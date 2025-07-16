
import pathlib
from conan import ConanFile
from conan.tools.files import copy
from conan.tools.google import Bazel
import os
import subprocess

class BazelConanRecipe(ConanFile):
    name = "bazel_conan_example"
    version = "0.1.0"
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "rust/*", "cpp/*", "WORKSPACE.bazel", "MODULE.bazel", "conan/*", "meta/*"
    generators = "BazelDeps", "BazelToolchain"
    requires = "fmt/11.2.0"

    def build(self):
        bazel = Bazel(self)
        bazel.build(target="meta:build_all")

    def package(self):
        # Export Rust binary
        rust_bin_dir = os.path.join(self.build_folder, "bazel-bin", "rust")
        copy(self, pattern="hello_world", dst=self.package_folder, src=rust_bin_dir, keep_path=False)
        # Export C++ binary
        cpp_bin_dir = os.path.join(self.build_folder, "bazel-bin", "cpp")
        copy(self, pattern="hello_fmt", dst=self.package_folder, src=cpp_bin_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.bindirs = ["."]
