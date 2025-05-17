#include "psf_reader.hpp"
#include <iostream>
#include <cstring>

psf_reader::psf_reader(const std::string& filename) : psf_file(filename) {
    if (psf_file.substr(psf_file.find_last_of(".") + 1) != "psf") {
        throw std::invalid_argument("File is not a PSF file");
    }
    if (!std::filesystem::exists(psf_file)) {
        throw std::invalid_argument("File does not exist");
    }
    if (std::filesystem::file_size(psf_file) == 0) {
        throw std::invalid_argument("File is empty");
    }

    f.open(psf_file, std::ios::binary);
    if (!f.is_open() || !f.good()) {
        throw std::runtime_error("File is not readable");
    }
}

psf_reader::~psf_reader() {
    if (f.is_open()) {
        f.close();
        std::cout << "File closed\n";
    }
}

PSFHeader psf_reader::get_header() {
    if (!f.is_open()) {
        throw std::runtime_error("File is not open");
    }

    uint8_t buf[32];
    f.read(reinterpret_cast<char*>(buf), sizeof(buf));

    uint32_t uiPSF = *reinterpret_cast<uint32_t*>(&buf[0]);
    std::string endian = (uiPSF == 0x50534600) ? "Little Endian" : "Big Endian";

    header = {
        uiPSF,
        endian,
        *reinterpret_cast<uint16_t*>(&buf[4]),
        *reinterpret_cast<uint16_t*>(&buf[6]),
        *reinterpret_cast<uint32_t*>(&buf[8]),
        *reinterpret_cast<uint32_t*>(&buf[12]),
        *reinterpret_cast<uint32_t*>(&buf[16]),
        *reinterpret_cast<uint16_t*>(&buf[20]),
        buf[22],
        buf[23],
        std::string(reinterpret_cast<char*>(&buf[24]), 8)
    };

    header.platformCfg.erase(header.platformCfg.find('\0'));

    return header;
}

void psf_reader::skip_white_space() {
    char b;
    while (f.read(&b, 1)) {
        if (b != '\x00') {
            f.seekg(-1, std::ios::cur); // rewind one byte
            break;
        }
    }
}

std::vector<uint32_t> psf_reader::read() {
    const size_t struct_size = 8;
    uint8_t buf[8];

    if (!f.read(reinterpret_cast<char*>(buf), struct_size)) {
        return {};
    }

    uint16_t eventID = *reinterpret_cast<uint16_t*>(&buf[0]);
    uint16_t eventCount = *reinterpret_cast<uint16_t*>(&buf[2]);
    uint32_t TS = *reinterpret_cast<uint32_t*>(&buf[4]);

    uint32_t param_count = (eventID >> 12) & 0xF;
    uint32_t event_id_lower = eventID & 0xFFF;

    std::vector<uint32_t> result = {param_count, event_id_lower, eventCount, TS};

    std::vector<uint32_t> params(param_count);
    if (!f.read(reinterpret_cast<char*>(params.data()), param_count * 4)) {
        throw std::runtime_error("Incomplete event data");
    }

    result.insert(result.end(), params.begin(), params.end());
    return result;
}

bool psf_reader::next(std::vector<uint32_t>& event_out) {
    event_out = read();
    return !event_out.empty();
}
