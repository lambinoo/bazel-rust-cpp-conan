# Bazel bzlmod + rules_rust Example

This project demonstrates a minimal Bazel setup using bzlmod and rules_rust for Rust builds.

## Usage

- Edit `MODULE.bazel` to manage dependencies.
- Add Rust code in the `rust/` directory (to be created).
- Build with: `bazel build //rust:hello_world`
