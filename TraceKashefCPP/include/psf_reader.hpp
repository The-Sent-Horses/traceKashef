#pragma once
#include <fstream>
#include <string>
#include <vector>
#include <stdexcept>
#include <cstdint>
#include <filesystem>

struct PSFHeader {
    uint32_t uiPSF;
    std::string endian;
    uint16_t uiVersion;
    uint16_t uiPlatform;
    uint32_t uiOptions;
    uint32_t uiNumCores;
    uint32_t isrTailchainingThreshold;
    uint16_t uiPlatformCfgPatch;
    uint8_t uiPlatformCfgMinor;
    uint8_t uiPlatformCfgMajor;
    std::string platformCfg;
};

class psf_reader {
public:
    explicit psf_reader(const std::string& filename);
    ~psf_reader();

    PSFHeader get_header();
    void skip_white_space();
    std::vector<uint32_t> read();
    bool next(std::vector<uint32_t>& event_out);

private:
    std::ifstream f;
    std::string psf_file;
    PSFHeader header;
};
