"""
gen_docs_site.py

Reads a docs.json file (shape produced by `rl docs --json`) and writes a
single-page HTML app with interactive sidebar, search, and no page reloads.

Usage:
    python3 gen_docs_site.py that_json.json output.html
"""

import html
import json
import sys


def esc(text):
    if text is None:
        return ""
    return html.escape(str(text))


def slugify(text):
    out = []
    for ch in str(text).lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " ._":
            out.append("-")
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "entry"


def func_name(sig):
    if not sig:
        return ""
    return sig.split("(")[0]


def render_fn_html(func):
    out = "<h3><code>" + esc(func.get("signature")) + "</code></h3>\n"
    since = func.get("since")
    updated = func.get("updated")
    if since:
        out += '<p class="meta"><em>since ' + esc(since)
        if updated:
            out += " | updated " + esc(updated)
        out += "</em></p>\n"
    deprecated = func.get("deprecated")
    if deprecated:
        out += "<p><strong>Deprecated:</strong> " + esc(deprecated) + "</p>\n"
    out += "<p>" + esc(func.get("description")) + "</p>\n"
    out += "<p><strong>Returns:</strong> " + esc(func.get("returns")) + "</p>\n"
    errors = func.get("errors")
    if errors:
        out += "<p><strong>Errors:</strong> " + esc(errors) + "</p>\n"
    example = func.get("example")
    if example:
        out += '<pre class="rl-code">' + esc(example) + "</pre>\n"
        expected = func.get("expected_output")
        if expected:
            out += "<p><em>output:</em></p>\n<pre>" + esc(expected) + "</pre>\n"
    see_also = func.get("see_also") or []
    if see_also:
        out += "<p><strong>See also:</strong> " + ", ".join(
            "<code>" + esc(n) + "</code>" for n in see_also
        ) + "</p>\n"
    return out


def render_desc_html(desc):
    out = ""
    title = desc.get("title")
    if title:
        out += "<h4>" + esc(title) + "</h4>\n"
    kind = desc.get("kind")
    kind_labels = {"Syntax": "Syntax", "Pitfall": "Pitfall", "Note": "Note"}
    label = kind_labels.get(kind)
    if label:
        out += "<p><strong>" + esc(label) + ":</strong> " + esc(desc.get("description")) + "</p>\n"
    else:
        out += "<p>" + esc(desc.get("description")) + "</p>\n"
    examples = desc.get("examples") or []
    expected_outputs = desc.get("expected_output") or []
    for i, example in enumerate(examples):
        expected = expected_outputs[i] if i < len(expected_outputs) else None
        out += '<pre class="rl-code">' + esc(example) + "</pre>\n"
        if expected:
            out += "<p><em>output:</em></p>\n<pre>" + esc(expected) + "</pre>\n"
    return out


def build_site(data, out_path):
    stdlib = data.get("stdlib") or []
    concepts = data.get("concepts") or []
    tutorial = data.get("tutorial") or []

    # Build all content sections as HTML strings, keyed by id
    contents = {}

    # --- Std Reference ---
    for mod in stdlib:
        mod_name = mod.get("name", "")
        mod_id = "std_" + slugify(mod_name)
        since = mod.get("since")
        unstable = mod.get("unstable")

        body = "<h1>std::" + esc(mod_name) + "</h1>\n"
        meta = []
        if since:
            meta.append("since " + esc(since))
        if unstable:
            meta.append("unstable")
        if meta:
            body += '<p class="meta"><em>' + " | ".join(meta) + "</em></p>\n"
        body += "<p>" + esc(mod.get("description")) + "</p>\n"
        funcs = mod.get("functions") or []
        if funcs:
            body += "<h2>Functions</h2>\n<ul>\n"
            for func in funcs:
                func_bare = func_name(func.get("signature", ""))
                func_id = mod_id + "_" + slugify(func_bare)
                body += '<li><a href="#" onclick="showContent(\'' + func_id + '\'); return false;"><code>' + esc(func_bare) + "</code></a></li>\n"
                func_body = "<h1>std::" + esc(mod_name) + "::" + esc(func_bare) + "</h1>\n"
                func_body += '<p class="meta"><em>module: <code>std::' + esc(mod_name) + "</code></em></p>\n"
                func_body += render_fn_html(func)
                contents[func_id] = func_body
            body += "</ul>\n"
        contents[mod_id] = body

    # --- Concepts ---
    for entry in concepts:
        name = entry.get("name", "")
        cid = "concept_" + slugify(name)
        body = "<h1>" + esc(name) + "</h1>\n"
        cat = entry.get("category", "")
        since = entry.get("since")
        meta = [esc(cat)]
        if since:
            meta.append("since " + esc(since))
        body += '<p class="meta"><em>' + " | ".join(meta) + "</em></p>\n"
        summary = entry.get("summary")
        if summary:
            body += "<p>" + esc(summary) + "</p>\n"
        for desc in entry.get("descriptions") or []:
            body += render_desc_html(desc)
        pitfalls = entry.get("pitfalls") or []
        if pitfalls:
            body += "<p><strong>Pitfalls:</strong></p>\n<ul>\n"
            for p in pitfalls:
                body += "<li>" + esc(p) + "</li>\n"
            body += "</ul>\n"
        contents[cid] = body

    # --- Tutorial ---
    for entry in tutorial:
        name = entry.get("name", "")
        tid = "tutorial_" + slugify(name)
        body = "<h1>" + esc(name) + "</h1>\n"
        since = entry.get("since")
        if since:
            body += '<p class="meta"><em>since ' + esc(since) + "</em></p>\n"
        summary = entry.get("summary")
        if summary:
            body += "<p>" + esc(summary) + "</p>\n"
        for desc in entry.get("descriptions") or []:
            body += render_desc_html(desc)
        contents[tid] = body

    # --- Build sidebar data structure for JS ---
    sidebar_data = []

    # Std Reference
    std_node = {"label": "Std Reference", "color": "#6cb0f5", "children": []}
    # Group by top-level module
    top_level = {}
    sub_modules = {}
    for mod in stdlib:
        name = mod.get("name", "")
        if "::" in name:
            parent = name.split("::")[0]
            sub_modules.setdefault(parent, []).append(mod)
        else:
            top_level[name] = mod

    for name in sorted(top_level.keys()):
        mod = top_level[name]
        mod_id = "std_" + slugify(name)
        funcs = mod.get("functions") or []

        if name in sub_modules:
            mod_node = {"label": name, "id": mod_id, "color": "#6cb0f5", "children": [
                {"label": name + " (overview)", "id": mod_id, "color": "#6cb0f5"}
            ]}
            for sub in sub_modules[name]:
                sub_name = sub.get("name", "")
                sub_short = sub_name.split("::")[-1]
                sub_id = "std_" + slugify(sub_name)
                sub_node = {"label": sub_short, "id": sub_id, "color": "#6cb0f5", "children": [
                    {"label": sub_short + " (overview)", "id": sub_id, "color": "#6cb0f5"}
                ]}
                for func in sub.get("functions") or []:
                    bare = func_name(func.get("signature", ""))
                    func_id = sub_id + "_" + slugify(bare)
                    sub_node["children"].append({"label": bare, "id": func_id, "color": "#6cb0f5"})
                mod_node["children"].append(sub_node)
            std_node["children"].append(mod_node)
        else:
            mod_node = {"label": name, "id": mod_id, "color": "#6cb0f5", "children": [
                {"label": name + " (overview)", "id": mod_id, "color": "#6cb0f5"}
            ]}
            for func in funcs:
                bare = func_name(func.get("signature", ""))
                func_id = mod_id + "_" + slugify(bare)
                mod_node["children"].append({"label": bare, "id": func_id, "color": "#6cb0f5"})
            std_node["children"].append(mod_node)
    sidebar_data.append(std_node)

    # Concepts
    cats = {}
    for e in concepts:
        cat = e.get("category", "Other")
        cats.setdefault(cat, []).append(e)
    cat_order = ["Syntax", "Types", "Control Flow", "Functions", "Modules", "Error Handling", "Tooling"]
    for cat in cats:
        if cat not in cat_order:
            cat_order.append(cat)

    concepts_node = {"label": "Concepts", "color": "#8cb4e0", "children": []}
    for cat in cat_order:
        if cat not in cats:
            continue
        cat_node = {"label": cat, "color": "#8cb4e0", "children": []}
        for e in cats[cat]:
            name = e.get("name", "")
            cat_node["children"].append({"label": name, "id": "concept_" + slugify(name), "color": "#8cb4e0"})
        concepts_node["children"].append(cat_node)
    sidebar_data.append(concepts_node)

    # Tutorial
    beginner = [e for e in tutorial if e.get("name", "")[:1].isdigit()]
    advanced = [e for e in tutorial if not e.get("name", "")[:1].isdigit()]
    tutorial_node = {"label": "Tutorial", "color": "#e0c068", "children": []}
    if beginner:
        beg_node = {"label": "Beginner", "color": "#e0c068", "children": []}
        for e in beginner:
            name = e.get("name", "")
            beg_node["children"].append({"label": name, "id": "tutorial_" + slugify(name), "color": "#e0c068"})
        tutorial_node["children"].append(beg_node)
    if advanced:
        adv_node = {"label": "Advanced", "color": "#e0c068", "children": []}
        for e in advanced:
            name = e.get("name", "")
            adv_node["children"].append({"label": name, "id": "tutorial_" + slugify(name), "color": "#e0c068"})
        tutorial_node["children"].append(adv_node)
    sidebar_data.append(tutorial_node)

    contents_json = json.dumps(contents)
    sidebar_json = json.dumps(sidebar_data)

    html_out = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>rl docs</title>
<style>
:root {
    --bg: #0d1420;
    --bg-alt: #0a1018;
    --panel: #0a121f;
    --border: #1e2d42;
    --text: #dbe4ee;
    --text-dim: #8ea0b8;
    --heading: #f2f6fb;
    --accent: #6cb0f5;
    --active-bg: #17395e;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    line-height: 1.65;
    color: var(--text);
    background: var(--bg);
    -webkit-font-smoothing: antialiased;
}

/* layout */
.layout { display: flex; height: 100vh; }

/* sidebar */
.sidebar {
    width: 300px;
    flex-shrink: 0;
    background: var(--bg-alt);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    overflow: hidden;
}
.sidebar-header {
    padding: 1rem 1rem 0.5rem;
    border-bottom: 1px solid var(--border);
}
.sidebar-header h1 {
    font-size: 1.1rem;
    color: var(--accent);
    margin-bottom: 0.5rem;
}
.search-box {
    width: 100%;
    padding: 0.4rem 0.6rem;
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text);
    font-size: 0.9rem;
    outline: none;
}
.search-box:focus { border-color: var(--accent); }
.search-box::placeholder { color: var(--text-dim); }
.sidebar-tree {
    flex: 1;
    overflow-y: auto;
    padding: 0.5rem 0;
}
.sidebar-tree::-webkit-scrollbar { width: 6px; }
.sidebar-tree::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

/* tree nodes */
.tree-group { user-select: none; }
.tree-label {
    display: flex;
    align-items: center;
    gap: 0.3em;
    padding: 0.25rem 0.8rem;
    cursor: pointer;
    font-size: 0.9rem;
    font-weight: 600;
    border-radius: 4px;
    margin: 0 0.3rem;
    transition: background 0.1s;
}
.tree-label:hover { background: #16253a; }
.tree-label.active { background: var(--active-bg); color: #fff; }
.tree-arrow {
    font-size: 0.6em;
    color: var(--text-dim);
    transition: transform 0.15s;
    flex-shrink: 0;
    width: 1em;
    text-align: center;
}
.tree-group.open > .tree-label .tree-arrow { transform: rotate(90deg); }
.tree-children {
    display: none;
    padding-left: 0.8rem;
}
.tree-group.open > .tree-children { display: block; }
.tree-leaf {
    padding: 0.2rem 0.8rem 0.2rem 1.4rem;
    cursor: pointer;
    font-size: 0.88rem;
    border-radius: 4px;
    margin: 0 0.3rem;
    transition: background 0.1s;
}
.tree-leaf:hover { background: #16253a; }
.tree-leaf.active { background: var(--active-bg); color: #fff; }

/* content */
.content {
    flex: 1;
    overflow-y: auto;
    padding: 2.5rem 3rem 4rem;
    max-width: 900px;
}
.content h1 {
    font-size: 1.8rem;
    color: var(--heading);
    border-bottom: 2px solid var(--border);
    padding-bottom: 0.4rem;
    margin-bottom: 1rem;
}
.content h2 {
    font-size: 1.3rem;
    color: var(--heading);
    margin-top: 2rem;
    border-bottom: 1px solid var(--border);
    padding-bottom: 0.2rem;
}
.content h3 {
    font-size: 1.05rem;
    color: var(--heading);
    margin-top: 1.5rem;
}
.content h4 {
    font-size: 0.95rem;
    color: var(--heading);
    margin-top: 1.2rem;
}
.content p { margin: 0.7rem 0; }
.content a { color: var(--accent); text-decoration: none; }
.content a:hover { text-decoration: underline; }
.content code {
    background: #16253a;
    padding: 0.12rem 0.35rem;
    border-radius: 4px;
    font-family: "SF Mono", Consolas, monospace;
    font-size: 0.88em;
    color: #cfe0f2;
}
.content pre {
    background: var(--panel);
    color: #d4dbe6;
    padding: 0.9rem 1rem;
    border-radius: 8px;
    overflow-x: auto;
    font-family: "SF Mono", Consolas, monospace;
    font-size: 0.88em;
    border: 1px solid var(--border);
    margin: 0.6rem 0;
}
.content pre code { background: none; padding: 0; }
.content .meta { color: var(--text-dim); }
.content strong { color: var(--heading); }
.content ul { padding-left: 1.4rem; }
.content li { margin: 0.2rem 0; }

/* syntax highlighting */
.rl-kw { color: #c896e8; }
.rl-type { color: #5fd0c0; }
.rl-lit { color: #c896e8; }
.rl-ident { color: #d4dbe6; }
.rl-string { color: #a8d18f; }
.rl-char { color: #a8d18f; }
.rl-number { color: #e0c068; }
.rl-comment { color: #7fa06a; font-style: italic; }
.rl-op { color: #d4dbe6; }

/* mobile */
.menu-toggle {
    display: none;
    position: fixed;
    top: 0.7rem;
    left: 0.7rem;
    z-index: 60;
    background: var(--bg-alt);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 0.4rem;
    cursor: pointer;
    color: var(--text);
    font-size: 1.2rem;
}
.sidebar-backdrop {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.5);
    z-index: 40;
}
@media (max-width: 860px) {
    .menu-toggle { display: block; }
    .sidebar {
        position: fixed;
        top: 0; left: 0; height: 100vh;
        transform: translateX(-100%);
        transition: transform 0.2s ease;
        z-index: 50;
        box-shadow: 2px 0 16px rgba(0,0,0,0.4);
    }
    .sidebar.open { transform: translateX(0); }
    .sidebar-backdrop.open { display: block; }
    .content { padding: 3rem 1.2rem 3rem; max-width: 100%; }
}
</style>
</head>
<body>
<button class="menu-toggle" onclick="toggleSidebar()">&#9776;</button>
<div class="sidebar-backdrop" onclick="toggleSidebar()"></div>
<div class="layout">
<nav class="sidebar">
    <div class="sidebar-header">
        <h1>rl docs</h1>
        <input class="search-box" type="text" placeholder="/ search..." id="search" oninput="onSearch(this.value)">
    </div>
    <div class="sidebar-tree" id="tree"></div>
</nav>
<div class="content" id="content">
    <h1>rl docs</h1>
    <p>Pick an item from the sidebar to get started.</p>
</div>
</div>

<script>
var CONTENTS = CONTENTS_PLACEHOLDER;
var TREE = TREE_PLACEHOLDER;
var activeId = null;

function buildTree(nodes, container) {
    nodes.forEach(function(node) {
        if (node.children && node.children.length > 0) {
            var group = document.createElement("div");
            group.className = "tree-group";

            var label = document.createElement("div");
            label.className = "tree-label";
            label.style.color = node.color || "#dbe4ee";
            label.innerHTML = '<span class="tree-arrow">&#9654;</span>' + escapeHtml(node.label);
            label.onclick = function(e) {
                e.stopPropagation();
                group.classList.toggle("open");
            };
            group.appendChild(label);

            var children = document.createElement("div");
            children.className = "tree-children";
            buildTree(node.children, children);
            group.appendChild(children);
            container.appendChild(group);
        } else {
            var leaf = document.createElement("div");
            leaf.className = "tree-leaf";
            leaf.style.color = node.color || "#dbe4ee";
            leaf.textContent = node.label;
            leaf.dataset.id = node.id;
            leaf.onclick = function(e) {
                e.stopPropagation();
                showContent(node.id, leaf);
            };
            container.appendChild(leaf);
        }
    });
}

function showContent(id, el) {
    if (!id || !CONTENTS[id]) return;
    // update active state
    document.querySelectorAll(".tree-leaf.active").forEach(function(e) { e.classList.remove("active"); });
    if (el) el.classList.add("active");
    activeId = id;

    var content = document.getElementById("content");
    content.innerHTML = CONTENTS[id];
    highlightCode(content);
    content.scrollTop = 0;
}

function onSearch(query) {
    var tree = document.getElementById("tree");
    tree.innerHTML = "";
    if (!query) {
        buildTree(TREE, tree);
        return;
    }
    var q = query.toLowerCase();
    var filtered = filterTree(TREE, q);
    buildTree(filtered, tree);
    // auto-expand all groups
    tree.querySelectorAll(".tree-group").forEach(function(g) { g.classList.add("open"); });
}

function filterTree(nodes, query) {
    var result = [];
    nodes.forEach(function(node) {
        if (node.children && node.children.length > 0) {
            var filteredChildren = filterTree(node.children, query);
            if (filteredChildren.length > 0) {
                result.push({label: node.label, color: node.color, children: filteredChildren});
            }
        } else {
            if (node.label.toLowerCase().indexOf(query) !== -1) {
                result.push(node);
            }
        }
    });
    return result;
}

function toggleSidebar() {
    document.querySelector(".sidebar").classList.toggle("open");
    document.querySelector(".sidebar-backdrop").classList.toggle("open");
}

function escapeHtml(s) {
    var d = document.createElement("div");
    d.textContent = s;
    return d.innerHTML;
}

function highlightCode(root) {
    var blocks = root.querySelectorAll("pre.rl-code");
    for (var i = 0; i < blocks.length; i++) {
        var block = blocks[i];
        block.innerHTML = highlight(block.textContent);
    }
}

function highlight(source) {
    var KW = new Set(["fn","for","while","return","continue","break","get","from","in","or","and","null","dec","if","else","as","match","CONST","loop","impl"]);
    var TY = new Set(["int","float","bool","string","byte","char","arr","error","result","uint"]);
    var LT = new Set(["true","false","ok","err"]);
    function match(re, s) { var m = re.exec(s); return m && m[0].length > 0 ? m[0] : null; }
    var NL = String.fromCharCode(10);
    var out = [], pos = 0;
    while (pos < source.length) {
        var rest = source.slice(pos), m = null, cls = "";
        if ((m = match(/^\\/\\/[^\\n]*/, rest))) { cls = "rl-comment"; }
        else if ((m = match(/^"(?:[^"\\\\]|\\\\.)*"/, rest))) { cls = "rl-string"; }
        else if ((m = match(/^'(?:[^'\\\\]|\\\\.)*'/, rest))) { cls = "rl-char"; }
        else if ((m = match(/^\\d+\\.\\d+|^\\d+/, rest))) { cls = "rl-number"; }
        else if ((m = match(/^[A-Za-z_][A-Za-z0-9_]*/, rest))) {
            cls = KW.has(m) ? "rl-kw" : TY.has(m) ? "rl-type" : LT.has(m) ? "rl-lit" : "rl-ident";
        }
        else if ((m = match(/^(==|!=|<=|>=|->|=>|\\+=|-=|\\*=|\\/\\=|::|\\.\\.|[\\+\\-\\*\\/=<>!?&|.,:;(){}\\[\\]])/, rest))) { cls = "rl-op"; }
        else if ((m = match(/^\\s+/, rest))) { out.push(escH(m)); pos += m.length; continue; }
        else { out.push(escH(source[pos])); pos++; continue; }
        out.push('<span class="'+cls+'">'+escH(m)+'</span>');
        pos += m.length;
    }
    return out.join("");
}

function escH(s) { return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

// Init
buildTree(TREE, document.getElementById("tree"));
</script>
</body>
</html>"""

    html_out = html_out.replace("CONTENTS_PLACEHOLDER", contents_json)
    html_out = html_out.replace("TREE_PLACEHOLDER", sidebar_json)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_out)

    print("Wrote " + out_path + " (" + str(len(contents)) + " sections)")


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 gen_docs_site.py <input.json> <output.html>", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = json.load(f)

    build_site(data, sys.argv[2])


if __name__ == "__main__":
    main()
