# The Book

The official rl-lang documentation site generator.

Reads the JSON dump produced by `rl docs --json` (the language reference,
stdlib docs, and tutorials baked into the `rl` binary) and renders it into a
static, multi-page HTML site with a navy theme, a sidebar linking every
entry, and client-side syntax highlighting for `rl` code blocks. No build
step, no frontend framework - plain HTML/CSS/JS.

Read it at: https://rl-lang.github.io/the-book

## How it fits together

- **`gen_docs_site.py`** - the generator. Takes a `docs.json` file and an
  output directory, and writes one `index.html` plus one page per stdlib
  module, concept, and tutorial entry, all cross-linked via the sidebar.
- **`style.css`** - navy color scheme, sidebar layout, and the token colors
  used by the syntax highlighter.
- **`rl-highlight.js`** - a small dependency-free tokenizer that highlights
  `<pre class="rl-code">` blocks client-side, based on the real keyword list
  from `rl-lang`'s lexer.
- **`.github/workflows/build-docs-site.yml`** - on every push to `main`,
  clones `rl-lang/rl-lang`, builds it with `cargo build --release`, runs
  `rl docs --json --output --out-file docs.json` to get a fresh doc dump,
  runs it through `gen_docs_site.py`, and deploys the result to GitHub Pages.

## Building locally

You need a `docs.json` file to feed the generator. Get one by building
[`rl-lang/rl-lang`](https://github.com/rl-lang/rl-lang) yourself and running:

```bash
cargo build --release
./target/release/rl docs --json --output --out-file docs.json
```

Then generate the site:

```bash
python3 gen_docs_site.py docs.json site_out
```

`gen_docs_site.py` copies `style.css` and `rl-highlight.js` into `site_out`
automatically - they just need to be sitting next to the script when you run
it. Serve the result to view it (opening `index.html` directly as a
`file://` URL also works, since there's no build step):

```bash
python3 -m http.server --directory site_out
```

Then open `http://localhost:8000`.

## Requirements

- Python 3, no third-party packages
- A build of [`rl-lang/rl-lang`](https://github.com/rl-lang/rl-lang) to
  produce `docs.json` (only needed locally - CI builds it for you)

## License

Documentation licensed under [CC BY 4.0](LICENSE).
