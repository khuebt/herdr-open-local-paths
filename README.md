# Herdr Open Local Paths

Open local files and folders from Herdr terminal links using Linux's default applications. Paths stay readable, without visible escape codes or decorative characters.

**Compatibility:** stock Herdr 0.9.5 only sends recognized URI links to plugins. Clicking plain paths such as `docs/plan.md` requires the companion [Herdr core patch](docs/core-patch.md). Installing this plugin alone does not add plain-path detection to stock Herdr.

## Requirements

- Linux desktop with `xdg-open` available.
- Python 3.10 or newer. No Python packages are required.
- Herdr 0.9.5 or newer. The companion patch targets one specific 0.9.5 commit; compatibility with later source versions must be verified separately.

## Install

```sh
herdr plugin install khuebt/herdr-open-local-paths
herdr plugin list --plugin khuebt.open-local-paths
```

For a local checkout:

```sh
git clone https://github.com/khuebt/herdr-open-local-paths.git
cd herdr-open-local-paths
herdr plugin link "$PWD"
```

With the patched core running, hold Ctrl and click `README.md`, `docs/core-patch.md` or `docs/`. Relative paths resolve against the clicked pane's working directory, not the plugin directory. Files open in their default application and folders in the file manager.

## Behavior and limits

- Existing absolute paths, relative paths and local `file://` targets are supported when Herdr passes them to the handler.
- A trailing `:line` or `:line:column` is removed only if the literal filename does not exist. Jumping to a line in the default app is not implemented.
- Missing targets, empty paths, control characters, other URL schemes and remote file URI hosts are rejected.
- Plain path detection uses ASCII. Explicit URI metadata can target names containing spaces or Unicode. Quoted paths with spaces have not been fully validated through terminal token selection.
- The plugin does not modify files, MIME associations or Herdr service configuration, and does not install or restart a server.

## Existing manual installation

The prototype used ID `local.open-paths`; this repository uses `khuebt.open-local-paths`. After installing this package, disable the prototype to avoid overlapping handlers:

```sh
herdr plugin disable local.open-paths
```

Migration is manual. Installing this package does not change other plugins automatically.

## Test

```sh
python3 test-open-path.py
python3 -m py_compile open-path.py test-open-path.py
```

Reference validation of the companion core patch covered 56 passing link tests, Clippy, live API file/folder activation and a user-confirmed physical Ctrl+click on an ASCII Markdown path on Ubuntu. This does not establish compatibility with every terminal or Herdr release.

## Marketplace

The repository is public; marketplace listing is deferred. Adding the `herdr-plugin` repository topic triggers marketplace discovery. Do that only after the [publication checklist](docs/marketplace.md) is complete.

## Remove

```sh
herdr plugin uninstall khuebt.open-local-paths
```

Removing this plugin does not remove the separate core patch or revert a manually configured custom Herdr binary.

## License

Apache-2.0. The companion patch derives from Herdr's Apache-2.0 source; see [NOTICE](NOTICE) and [LICENSE](LICENSE). This community project is not an official Herdr release.
