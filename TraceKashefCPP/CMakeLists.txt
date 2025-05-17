cmake_minimum_required(VERSION 3.14)
project(PSFReaderProject)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include header files
include_directories(include)

# Source files
add_library(psf_reader
    src/psf_reader.cpp
)

# Main test/executable
add_executable(psf_test
    test.cpp
    decoder/decoder.cpp
)

# Link libraries
target_link_libraries(psf_test
    psf_reader
)
