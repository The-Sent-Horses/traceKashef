from .PSF_EVENTS import PSF_EVENT

def event_check(event_name: PSF_EVENT, event:list, expected_params:int):
    
    if event[1] != event_name:
        raise ValueError(f"Not a {event_name.name} event, you provided {PSF_EVENT(event[1]).name}")


def extract_name_from_words(words):
    """
    Converts a list of 32-bit words (as integers) into a null-terminated ASCII string.

    Parameters:
        words (list[int]): List of integers (each 4 bytes representing part of the string).

    Returns:
        str: Decoded ASCII string up to the first null terminator.
    """
    name_bytes = bytearray()
    for word in words:
        name_bytes.extend(word.to_bytes(4, byteorder='little'))
    return name_bytes.split(b'\x00')[0].decode('ascii', errors='replace')

