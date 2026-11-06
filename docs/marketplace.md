# Marketplace publication checklist

The public repository is the distribution source. Marketplace listing is a later, explicit publishing step.

- [ ] Decide how users obtain plain-path support: upstream Herdr capability or an explicitly documented compatible custom build. Do not advertise plugin-only installation as sufficient on stock 0.9.5.
- [ ] Test GitHub installation on a clean Linux desktop and supported Python/Herdr versions.
- [ ] Verify file/folder clicks, pane CWD resolution, clean ASCII display, missing targets, web links and file URI behavior.
- [ ] Resolve or retain the documented quoted-space limitation. Keep remote-machine behavior explicit.
- [ ] Ensure CI passes and manifest compatibility/version metadata is accurate.
- [ ] Review license, provenance, install/uninstall and service deployment notes.
- [ ] Create a version tag/release for pinned installation when ready.
- [ ] After publication approval, add the `herdr-plugin` topic in the GitHub repository's About settings.
- [ ] Verify the listing in the [Herdr community marketplace](https://herdr.dev/tui/plugins/) states compatibility requirements correctly.

Herdr discovers public repositories through that topic. This repository keeps `herdr-plugin.toml` at its root. See [marketplace documentation](https://herdr.dev/tui/docs/marketplace/). The initial repository publication does not add the marketplace topic.
