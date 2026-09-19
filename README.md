# The Book

The official rl-lang documentation site generator.

Reads the JSON dump produced by `rl docs --json` (the language reference,
stdlib docs, and tutorials baked into the `rl` binary) and renders it into a
single-page interactive HTML app with a collapsible sidebar, search, inline
syntax highlighting for `rl` code blocks, and clickable "see also" links. No
build step, no frontend framework - one self-contained HTML file with embedded
JSON data and inline JS/CSS.

Read it at: https://rl-lang.github.io/the-book

## How it fits together

- **`gen_docs_site.py`** - the generator. Takes a `docs.json` file and an
  output path, and writes a single `index.html` with all content and code
  embedded inline. Each stdlib function, concept, and tutorial entry gets its
  own selectable page in the sidebar.
- **`style.css`** - navy color scheme, sidebar layout, and the token colors
  used by the syntax highlighter.
- **`rl-highlight.js`** - a small dependency-free tokenizer for highlighting
  `rl` code blocks (kept for reference; the generated site uses an inline copy).
- **`.github/workflows/build-docs-site.yml`** - on every push to `master`,
  clones `rl-lang/rl-lang`, builds `rldocs`, generates `docs.json`, runs it
  through `gen_docs_site.py`, and deploys the result to GitHub Pages.

## Building locally

You need a `docs.json` file to feed the generator. Get one by building
[`rl-lang/rl-lang`](https://github.com/rl-lang/rl-lang) yourself and running:

```bash
cargo build --release
./target/release/rldocs --json -o --out-file docs.json
```

Then generate the site:

```bash
python3 gen_docs_site.py docs.json index.html
```

Serve the result to view it (opening `index.html` directly as a `file://` URL
also works, since there's no build step):

```bash
python3 -m http.server
```

Then open `http://localhost:8000`.

## Features

- **Collapsible tree sidebar** - std modules expand to show individual
  functions; concepts group by category; tutorials split into beginner/advanced.
- **Per-function pages** - each stdlib function has its own page with full
  documentation (signature, description, examples, errors, see also).
- **Clickable "see also" links** - cross-references between functions navigate
  directly to the target page.
- **Inline code highlighting** - backtick-wrapped code in descriptions renders
  as `<code>` tags; code blocks get syntax-highlighted client-side.
- **Search** - filter the sidebar tree by typing in the search box.
- **Mobile-friendly** - hamburger menu toggles the sidebar on small screens.

## Requirements

- Python 3, no third-party packages
- A build of [`rl-lang/rl-lang`](https://github.com/rl-lang/rl-lang) to
  produce `docs.json` (only needed locally - CI builds it for you)

## License

Documentation licensed under [CC BY 4.0](LICENSE).
