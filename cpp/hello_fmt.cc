#include <fmt/core.h>
#include <iostream>

int main() {
    std::string who = "Bazel + Conan + fmt";
    std::cout << fmt::format("Hello, {}!", who) << std::endl;
    return 0;
}
