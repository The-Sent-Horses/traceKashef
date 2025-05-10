from .common import event_check
from .PSF_EVENTS import PSF_EVENT
from .common import event_check
from .PSF_EVENTS import PSF_EVENT

def interpret_free_event(event):
    event_check(PSF_EVENT.FREE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    memory_address = f"0x{event[4]:X}"
    memory_size = event[5]

    return [
        timestamp,
        event_type,
        memory_address,
        memory_size
    ]

def interpret_free_failed_event(event):
    event_check(PSF_EVENT.FREE_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    memory_address = f"0x{event[4]:X}"
    memory_size = event[5]

    return [
        timestamp,
        event_type,
        memory_address,
        memory_size
    ]

def interpret_malloc_event(event):
    event_check(PSF_EVENT.MALLOC, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    memory_address = f"0x{event[4]:X}"
    memory_size = event[5]

    return [
        timestamp,
        event_type,
        memory_address,
        memory_size
    ]

def interpret_malloc_failed_event(event):
    event_check(PSF_EVENT.MALLOC_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    memory_address = f"0x{event[4]:X}"  # will usually be 0x0
    memory_size = event[5]

    return [
        timestamp,
        event_type,
        memory_address,
        memory_size
    ]