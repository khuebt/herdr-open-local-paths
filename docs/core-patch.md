# Companion Herdr core patch

Stock Herdr 0.9.5 passes recognized URLs to `link_handlers`, but not ordinary path text. The patch adds ASCII path matching to the existing terminal hover and activation flow. The plugin resolves path text using `focused_pane_cwd` in Herdr's invocation context.

The patch targets [herdrdev/herdr commit ee5bfb5041bb3e4a49d591c72308aae3c81ecdde](https://github.com/herdrdev/herdr/tree/ee5bfb5041bb3e4a49d591c72308aae3c81ecdde). It is a local customization, not an upstream release. See the [upstream discussion](https://github.com/herdrdev/herdr/discussions/1699) about bare-path plugin support.

## Build and validate

Start in the parent directory containing the plugin checkout. Install Herdr's build prerequisites, including Zig 0.16.0, first. Rust is selected by its `rust-toolchain.toml`.

```sh
git clone https://github.com/herdrdev/herdr.git herdr-local-paths
cd herdr-local-paths
git checkout ee5bfb5041bb3e4a49d591c72308aae3c81ecdde
git apply --check ../herdr-open-local-paths/patches/herdr-0.9.5-local-paths.patch
git apply ../herdr-open-local-paths/patches/herdr-0.9.5-local-paths.patch
cargo test --locked --bin herdr link_ -- --test-threads=1
cargo clippy --locked --all-targets -- -D warnings
cargo build --release --locked
```

The executable is `target/release/herdr`. Building does not replace your running server. Test in an isolated session before changing a service.

## Systemd deployment

Do not use live handoff for a server managed by a systemd unit with `Type=simple` and `KillMode=control-group`. In the reference environment the old main process exited and systemd terminated the imported server in its cgroup. `setsid()` did not prevent cleanup; a foreground rehearsal did not reveal the service-specific failure.

For a managed service, review and back up its configuration and session data, point `ExecStart` at a persistent custom binary and arrange a controlled restart. Restarting stops pane processes; saved agent sessions may need to be resumed. This repository does not automate service changes or restarts.

Keep the original stable binary and rollback configuration. Do not delete a build while a service points to it. Later Herdr releases may require rebasing or removing the patch; do not assume it is included upstream.
