"""
gen_docs_site.py

Reads a docs.json file (shape produced by `rl docs --json`, i.e. the
DocsJson struct: { "stdlib": [...], "concepts": [...], "tutorial": [...] })
and writes a multi-page HTML site: one index.html plus one file per
stdlib module / concept / tutorial entry, all linked together.
No CSS, no JS.

Usage:
    python3 gen_docs_site.py that_json.json output_dir
"""

import html
import json
import os
import sys


def esc(text):
    if text is None:
        return ""
    return html.escape(str(text))


def slugify(text):
    """Turn a name into a safe filename/id (letters, digits, hyphens)."""
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


def page(title, sidebar_html, body):
    return (
        "<!DOCTYPE html>\n"
        "<html>\n"
        "<head>\n"
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>" + esc(title) + "</title>\n"
        '<link rel="stylesheet" href="style.css">\n'
        '<script src="rl-highlight.js" defer></script>\n'
        "</head>\n"
        "<body>\n"
        '<header class="topbar">\n'
        '<button class="menu-toggle" type="button" aria-label="Toggle navigation" aria-expanded="false">\n'
        "<span></span><span></span><span></span>\n"
        "</button>\n"
        '<a class="topbar-brand" href="index.html">rl docs</a>\n'
        "</header>\n"
        '<div class="layout">\n'
        '<div class="sidebar-backdrop"></div>\n'
        '<nav class="sidebar">\n' + sidebar_html + "</nav>\n"
        "<main>\n" + body + "</main>\n"
        "</div>\n"
        "<script>\n"
        "(function(){\n"
        '  var btn = document.querySelector(".menu-toggle");\n'
        '  var sidebar = document.querySelector(".sidebar");\n'
        '  var backdrop = document.querySelector(".sidebar-backdrop");\n'
        "  function close(){\n"
        '    sidebar.classList.remove("open");\n'
        '    backdrop.classList.remove("open");\n'
        '    btn.setAttribute("aria-expanded", "false");\n'
        "  }\n"
        "  function toggle(){\n"
        '    var open = sidebar.classList.toggle("open");\n'
        '    backdrop.classList.toggle("open", open);\n'
        '    btn.setAttribute("aria-expanded", open ? "true" : "false");\n'
        "  }\n"
        '  btn.addEventListener("click", toggle);\n'
        '  backdrop.addEventListener("click", close);\n'
        '  sidebar.addEventListener("click", function(e){\n'
        '    if (e.target.tagName === "A") close();\n'
        "  });\n"
        "})();\n"
        "</script>\n"
        "</body>\n"
        "</html>\n"
    )


def render_example_block(example, expected_output):
    out = '<pre class="rl-code">' + esc(example) + "</pre>\n"
    if expected_output:
        out += "<p><em>output:</em></p>\n"
        out += "<pre>" + esc(expected_output) + "</pre>\n"
    return out


def render_related(label, names, link_map=None, prefix=""):
    """
    Render a labeled list of related names.
    link_map, if given, is {name: filename} so related items become links
    to their own page instead of plain text.
    """
    if not names:
        return ""
    items = []
    for n in names:
        display = esc(prefix + n)
        if link_map and n in link_map:
            items.append(
                '<a href="' + esc(link_map[n]) + '"><code>' + display + "</code></a>"
            )
        else:
            items.append("<code>" + display + "</code>")
    return "<p><strong>" + esc(label) + ":</strong> " + ", ".join(items) + "</p>\n"


def render_fn_entry(func, fn_link_map):
    out = "<h3><code>" + esc(func.get("signature")) + "</code></h3>\n"
    since = func.get("since")
    if since:
        out += "<p><em>since " + esc(since) + "</em></p>\n"
    out += "<p>" + esc(func.get("description")) + "</p>\n"
    out += "<p><strong>Returns:</strong> " + esc(func.get("returns")) + "</p>\n"
    errors = func.get("errors")
    if errors:
        out += "<p><strong>Errors:</strong> " + esc(errors) + "</p>\n"

    example = func.get("example")
    if example:
        out += render_example_block(example, func.get("expected_output"))

    out += render_related("See also", func.get("see_also") or [], fn_link_map)
    return out


def render_description_entry(desc):
    out = ""
    title = desc.get("title")
    if title:
        out += "<h4>" + esc(title) + "</h4>\n"

    kind = desc.get("kind")
    kind_labels = {"Syntax": "Syntax", "Pitfall": "Pitfall", "Note": "Note"}
    label = kind_labels.get(kind)
    if label:
        out += (
            "<p><strong>"
            + esc(label)
            + ":</strong> "
            + esc(desc.get("description"))
            + "</p>\n"
        )
    else:
        out += "<p>" + esc(desc.get("description")) + "</p>\n"

    examples = desc.get("examples") or []
    expected_outputs = desc.get("expected_output") or []
    for i, example in enumerate(examples):
        expected = expected_outputs[i] if i < len(expected_outputs) else None
        out += render_example_block(example, expected)

    return out


class SiteBuilder:
    def __init__(self, data, out_dir):
        self.stdlib = data.get("stdlib") or []
        self.concepts = data.get("concepts") or []
        self.tutorial = data.get("tutorial") or []
        self.out_dir = out_dir

        # filename maps, so cross-references (see_also / related / related_stdlib)
        # can become real links between pages
        self.std_files = {
            e.get("name", ""): "std_" + slugify(e.get("name", "")) + ".html"
            for e in self.stdlib
        }
        self.concept_files = {
            e.get("name", ""): "concept_" + slugify(e.get("name", "")) + ".html"
            for e in self.concepts
        }
        self.tutorial_files = {
            e.get("name", ""): "tutorial_" + slugify(e.get("name", "")) + ".html"
            for e in self.tutorial
        }

        # flat map of every function's bare name -> its module page, for "see also" links
        self.fn_files = {}
        for e in self.stdlib:
            fname = self.std_files[e.get("name", "")]
            for func in e.get("functions") or []:
                sig = func.get("signature", "")
                bare = sig.split("(")[0] if sig else sig
                self.fn_files[bare] = fname

    def sidebar_html(self, active_filename=None):
        """
        Builds the full sidebar shown on every page: a Home link plus
        one section per category (stdlib/concepts/tutorial), each listing
        every entry. The current page's link gets the 'active' class.
        """

        def link(filename, label):
            cls = ' class="active"' if filename == active_filename else ""
            return (
                '<li><a href="'
                + esc(filename)
                + '"'
                + cls
                + ">"
                + esc(label)
                + "</a></li>\n"
            )

        out = '<a class="home-link" href="index.html">rl docs</a>\n'

        if self.stdlib:
            out += "<h2>stdlib</h2>\n<ul>\n"
            for e in self.stdlib:
                name = e.get("name", "")
                out += link(self.std_files[name], "std::" + name)
            out += "</ul>\n"

        if self.concepts:
            out += "<h2>concepts</h2>\n<ul>\n"
            for e in self.concepts:
                name = e.get("name", "")
                out += link(self.concept_files[name], name)
            out += "</ul>\n"

        if self.tutorial:
            out += "<h2>tutorial</h2>\n<ul>\n"
            for e in self.tutorial:
                name = e.get("name", "")
                out += link(self.tutorial_files[name], name)
            out += "</ul>\n"

        return out

    def write(self, filename, title, body):
        content = page(title, self.sidebar_html(active_filename=filename), body)
        with open(os.path.join(self.out_dir, filename), "w", encoding="utf-8") as f:
            f.write(content)

    def build_index(self):
        body = "<h1>rl docs</h1>\n"
        if self.stdlib or self.concepts or self.tutorial:
            body += "<p>Pick an item from the sidebar to get started.</p>\n"
        else:
            body += "<p>No documentation entries found in this JSON file.</p>\n"

        content = page("rl docs", self.sidebar_html(active_filename="index.html"), body)
        with open(os.path.join(self.out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(content)

    def build_std_page(self, entry):
        name = entry.get("name", "")
        body = "<h1>std::" + esc(name) + "</h1>\n"

        meta_bits = []
        since = entry.get("since")
        if since:
            meta_bits.append("since " + esc(since))
        if entry.get("unstable"):
            meta_bits.append("unstable")
        if meta_bits:
            body += "<p><em>" + " | ".join(meta_bits) + "</em></p>\n"

        body += "<p>" + esc(entry.get("description")) + "</p>\n"

        for func in entry.get("functions") or []:
            body += render_fn_entry(func, self.fn_files)

        self.write(self.std_files[name], "std::" + name, body)

    def build_concept_or_tutorial_page(self, entry, file_map):
        name = entry.get("name", "")
        body = "<h1>" + esc(name) + "</h1>\n"

        meta_bits = [esc(entry.get("category"))]
        since = entry.get("since")
        if since:
            meta_bits.append("since " + esc(since))
        body += "<p><em>" + " | ".join(meta_bits) + "</em></p>\n"

        summary = entry.get("summary")
        if summary:
            body += "<p>" + esc(summary) + "</p>\n"

        body += render_related(
            "Prerequisites", entry.get("prerequisites") or [], self.concept_files
        )

        for desc in entry.get("descriptions") or []:
            body += render_description_entry(desc)

        pitfalls = entry.get("pitfalls") or []
        if pitfalls:
            body += "<p><strong>Pitfalls:</strong></p>\n<ul>\n"
            for p in pitfalls:
                body += "<li>" + esc(p) + "</li>\n"
            body += "</ul>\n"

        body += render_related(
            "Related concepts", entry.get("related") or [], self.concept_files
        )
        body += render_related(
            "Related stdlib", entry.get("related_stdlib") or [], self.std_files, "std::"
        )

        self.write(file_map[name], name, body)

    def build(self):
        os.makedirs(self.out_dir, exist_ok=True)
        self._copy_asset("style.css")
        self._copy_asset("rl-highlight.js")
        self.build_index()
        for entry in self.stdlib:
            self.build_std_page(entry)
        for entry in self.concepts:
            self.build_concept_or_tutorial_page(entry, self.concept_files)
        for entry in self.tutorial:
            self.build_concept_or_tutorial_page(entry, self.tutorial_files)

    def _copy_asset(self, filename):
        """Copy a static asset (css/js) that ships alongside this script
        into the output directory."""
        src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        dst_path = os.path.join(self.out_dir, filename)

        if not os.path.exists(src_path):
            print(
                "WARNING: could not find " + filename + " next to gen_docs_site.py "
                "(looked at " + src_path + "). The site will link to it but the "
                "file won't exist in the output.",
                file=sys.stderr,
            )
            return

        if os.path.abspath(src_path) == os.path.abspath(dst_path):
            print("note: " + filename + " already in output dir, skipping copy")
            return

        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("copied " + filename + " -> " + dst_path)


def main():
    if len(sys.argv) < 3:
        print(
            "Usage: python3 gen_docs_site.py <input.json> <output_dir>", file=sys.stderr
        )
        sys.exit(1)

    input_path = sys.argv[1]
    out_dir = sys.argv[2]

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    builder = SiteBuilder(data, out_dir)
    builder.build()

    print(
        "Wrote site to "
        + out_dir
        + "/ ("
        + str(1 + len(builder.stdlib) + len(builder.concepts) + len(builder.tutorial))
        + " pages)"
    )


if __name__ == "__main__":
    main()
