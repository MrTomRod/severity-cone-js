# Development

Notes for working on the cone files and checking the site locally.

## Local preview

GitHub Pages serves this folder as plain static files, so a local HTTP server is an
accurate preview:

```sh
python3 -m http.server 8000   # then open http://localhost:8000/cone.html
```

To check paths under a project URL (`/<repo>/…`) before pushing, serve the parent
directory and open `http://localhost:8000/<repo>/`:

```sh
mkdir -p /tmp/gh-root && ln -sfn "$PWD" /tmp/gh-root/my-repo
python3 -m http.server 8000 -d /tmp/gh-root
```

For the rendered README rather than raw file listings:

```sh
uvx --from grip grip README.md   # http://localhost:6419
```

`index.html` redirects to `cone.html`, so the Pages root is usable. `.nojekyll` keeps
Jekyll out of the way.

## Regenerating the state images

The SVGs are the source of truth. After editing a `cone-*.svg`, run `python3 make-states.py` to refresh `states/`.
