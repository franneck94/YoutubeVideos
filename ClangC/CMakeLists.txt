cmake_minimum_required(VERSION 3.16)

project(ExampleProjectC)

set(CMAKE_C_STANDARD c99)

add_library(CsvReader)

target_include_directories(CsvReader PUBLIC
    inc/
)
target_sources(CsvReader PUBLIC
    src/CsvReader.c
    src/Record.c
)

add_executable(CsvExecutable app/Main.c)

target_link_libraries(CsvExecutable CsvReader)

set(CMAKE_C_CLANG_TIDY clang-tidy)
