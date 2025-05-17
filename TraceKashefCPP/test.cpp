#include "psf_reader.hpp"
#include <iostream>

int main() {
    try {
        psf_reader reader("/mnt/c/Program Files/Percepio/Tracealyzer 4/FreeRTOS/demo_freertos.psf");

        auto header = reader.get_header();
        std::cout << "Endian: " << header.endian << ", Version: " << header.uiVersion << "\n";

        reader.skip_white_space();

        std::vector<uint32_t> event;
        while (reader.next(event)) {
            std::cout << "Event ID: " << event[1] << ", Params: ";
            for (size_t i = 4; i < event.size(); ++i)
                std::cout << event[i] << " ";
            std::cout << "\n";
        }

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << "\n";
    }

    return 0;
}
