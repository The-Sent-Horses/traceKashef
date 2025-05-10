import struct
import os

from .PSF_EVENTS import PSF_EVENT

TRACE_EVENT0_FMT = "<H H "  # 4 bytes
TRACE_EVENTN_FMT_BASE = "<H H I"  # Start of TraceEventN_t
TRACE_HEADER_FMT = "<I H H I I I H B B 8s"

class psf_reader: 
    
    def __init__(self, psf_file):
        self.psf_file = psf_file
        self.psf_header = {}
        self.f = open(self.psf_file, "rb")
        
        # check if the file is a PSF file
        if not self.psf_file.endswith(".psf"):
            raise ValueError("File is not a PSF file")
        # check if the file exists
        if not os.path.exists(self.psf_file):
            raise ValueError("File does not exist")
        # check if the file is empty
        if os.path.getsize(self.psf_file) == 0:
            raise ValueError("File is empty")
        # check if the file is readable
        if not os.access(self.psf_file, os.R_OK):
            raise ValueError("File is not readable")
            
            
    def __iter__(self):
        # Return the iterator object (self)
        return self 
        
    
    def get_header(self):
        # check if the file is open
        if not self.f:
            raise ValueError("File is not open")
        
        
        
        # Read and parse TraceHeader
        header_data = self.f.read(32)
        header = struct.unpack(TRACE_HEADER_FMT, header_data)
        
        uiPSF = header_data[0]
        endian = "Little Endian" if uiPSF == 0x50534600 else "Big Endian"

        self.psf_header = {
            "uiPSF": header[0],
            "endian": endian,
            "uiVersion": header[1],
            "uiPlatform": header[2],
            "uiOptions": header[3],
            "uiNumCores": header[4],
            "isrTailchainingThreshold": header[5],
            "uiPlatformCfgPatch": header[6],
            "uiPlatformCfgMinor": header[7],
            "uiPlatformCfgMajor": header[8],
            "platformCfg": header[9].decode(errors='ignore').strip('\x00')
        }
        
        
        return self.psf_header
    
    def skip_white_space(self):
        while True:
            byte = self.f.read(1)
            if not byte or byte != b'\x00':  # Stop at first non-null byte
                self.f.seek(-1, 1)  # Step back to the first real event byte
                break
    
    def read(self):
    
        struct_size = 8
        
            
        byte = self.f.read(struct_size)

        if len(byte) < struct_size:
            return None  # End of file or incomplete read
        eventID, eventCount, TS = struct.unpack(TRACE_EVENTN_FMT_BASE, byte) # "<H H I" 
        
        param_count = (eventID >> 12) & 0xF  # Assuming event ID encodes N (upper 4 bits)
        event_id_lower = eventID & 0xFFF  # Lower 12 bits for event ID
        
        param_format = f"<{param_count}I" # for reading the parameters if any
        param_size = param_count * 4  # 4 bytes per parameter
        param_data = self.f.read(param_size)
        params = []
        if len(param_data) < param_size:
            print("Incomplete event data")
            raise ValueError("Incomplete event data")
        params = struct.unpack(param_format, param_data)
        
        
        return [param_count, event_id_lower, eventCount, TS] + list(params)
    
    def __next__(self):
        # Read the next event from the file
        event = self.read()
        
        # Check if the end of the file is reached
        if not event:
            raise StopIteration
        
        # Return the event
        return event
    
    def __del__(self):
        # Close the file when the object is deleted
        if self.f:
            self.f.close()
            self.f = None
        print("File closed")

        