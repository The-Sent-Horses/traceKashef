from .common import event_check
from .PSF_EVENTS import PSF_EVENT
from .common import event_check
from .PSF_EVENTS import PSF_EVENT

def interpret_eventgroup_create_event(event):
    event_check(PSF_EVENT.EVENTGROUP_CREATE, event, 3)
    params = event[4:]
    eventgroup_pointer = params[0]
    dummy = params[1]
    initial_bits = params[2]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{eventgroup_pointer:X}",
        initial_bits
    ]

def interpret_eventgroup_sync_block_event(event):
    event_check(PSF_EVENT.EVENTGROUP_SYNC_BLOCK, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    eventgroup_pointer = f"0x{event[4]:X}"
    bits_to_wait_for = event[5]

    return [
        timestamp,
        event_type,
        eventgroup_pointer,
        bits_to_wait_for
    ]

def interpret_eventgroup_sync_event(event):
    event_check(PSF_EVENT.EVENTGROUP_SYNC, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    eventgroup_pointer = f"0x{event[4]:X}"
    bits_to_wait_for = event[5]

    return [
        timestamp,
        event_type,
        eventgroup_pointer,
        bits_to_wait_for
    ]

def interpret_eventgroup_sync_failed_event(event):
    event_check(PSF_EVENT.EVENTGROUP_SYNC_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    eventgroup_pointer = f"0x{event[4]:X}"
    bits_to_wait_for = event[5]

    return [
        timestamp,
        event_type,
        eventgroup_pointer,
        bits_to_wait_for
    ]

def interpret_eventgroup_waitbits_block_event(event):
    event_check(PSF_EVENT.EVENTGROUP_WAITBITS_BLOCK, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    eventgroup_pointer = f"0x{event[4]:X}"
    bits_to_wait_for = event[5]

    return [
        timestamp,
        event_type,
        eventgroup_pointer,
        bits_to_wait_for
    ]

def interpret_eventgroup_waitbits_event(event):
    event_check(PSF_EVENT.EVENTGROUP_WAITBITS, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    eventgroup_pointer = f"0x{event[4]:X}"
    bits_to_wait_for = event[5]

    return [
        timestamp,
        event_type,
        eventgroup_pointer,
        bits_to_wait_for
    ]

def interpret_eventgroup_waitbits_failed_event(event):
    event_check(PSF_EVENT.EVENTGROUP_WAITBITS_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    eventgroup_pointer = f"0x{event[4]:X}"
    bits_to_wait_for = event[5]

    return [
        timestamp,
        event_type,
        eventgroup_pointer,
        bits_to_wait_for
    ]

def interpret_eventgroup_clearbits_event(event):
    event_check(PSF_EVENT.EVENTGROUP_CLEARBITS, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    eventgroup_pointer = f"0x{event[4]:X}"
    bits_to_clear = event[5]

    return [
        timestamp,
        event_type,
        eventgroup_pointer,
        bits_to_clear
    ]

def interpret_eventgroup_clearbits_fromisr_event(event):
    event_check(PSF_EVENT.EVENTGROUP_CLEARBITS_FROMISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    eventgroup_pointer = f"0x{event[4]:X}"
    bits_to_clear = event[5]

    return [
        timestamp,
        event_type,
        eventgroup_pointer,
        bits_to_clear
    ]

def interpret_eventgroup_setbits_event(event):
    event_check(PSF_EVENT.EVENTGROUP_SETBITS, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    eventgroup_pointer = f"0x{event[4]:X}"
    bits_to_set = event[5]

    return [
        timestamp,
        event_type,
        eventgroup_pointer,
        bits_to_set
    ]

def interpret_eventgroup_setbits_fromisr_event(event):
    event_check(PSF_EVENT.EVENTGROUP_SETBITS_FROMISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    eventgroup_pointer = f"0x{event[4]:X}"
    bits_to_set = event[5]

    return [
        timestamp,
        event_type,
        eventgroup_pointer,
        bits_to_set
    ]

def interpret_eventgroup_delete_event(event):
    event_check(PSF_EVENT.EVENTGROUP_DELETE, event, 2)

    params = event[4:]
    eventgroup_pointer = params[0]
    current_bits = params[1]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{eventgroup_pointer:X}",
        current_bits
    ]

def interpret_eventgroup_create_failed_event(event):
    event_check(PSF_EVENT.EVENTGROUP_CREATE_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    pointer = f"0x{event[4]:X}"
    dummy = event[5]

    return [
        timestamp,
        event_type,
        pointer,
        dummy
    ]