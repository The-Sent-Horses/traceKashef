from .common import event_check, extract_name_from_words
from .PSF_EVENTS import PSF_EVENT

def interpret_mutex_create_event(event):
    event_check(PSF_EVENT.MUTEX_CREATE, event, 3)
    params = event[4:]
    mutex_pointer = params[0]
    dummy = params[1]
    name_words = params[2:]

    name = extract_name_from_words(name_words)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{mutex_pointer:X}",
        dummy,
        name
    ]

def interpret_mutex_recursive_create_event(event):
    event_check(PSF_EVENT.MUTEX_RECURSIVE_CREATE, event, 3)
    params = event[4:]
    mutex_pointer = params[0]
    dummy = params[1]
    name_words = params[2:]

    name = extract_name_from_words(name_words)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{mutex_pointer:X}",
        dummy,
        name
    ]

def interpret_mutex_delete_event(event):
    event_check(PSF_EVENT.MUTEX_DELETE, event, 2)

    params = event[4:]
    mutex_pointer = params[0]
    messages_waiting = params[1]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{mutex_pointer:X}",
        messages_waiting
    ]

def interpret_mutex_give_event(event):
    event_check(PSF_EVENT.MUTEX_GIVE, event, 1)

    mutex_pointer = event[4]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{mutex_pointer:X}"
    ]

def interpret_mutex_give_recursive_event(event):
    event_check(PSF_EVENT.MUTEX_GIVE_RECURSIVE, event, 1)

    mutex_pointer = event[4]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{mutex_pointer:X}"
    ]

def interpret_mutex_create_failed_event(event):
    event_check(PSF_EVENT.MUTEX_CREATE_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    mutex_pointer = f"0x{event[4]:X}"
    dummy = event[5]

    return [
        timestamp,
        event_type,
        mutex_pointer,
        dummy
    ]

def interpret_mutex_recursive_create_failed_event(event):
    event_check(PSF_EVENT.MUTEX_RECURSIVE_CREATE_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    mutex_pointer = f"0x{event[4]:X}"
    dummy = event[5]

    return [
        timestamp,
        event_type,
        mutex_pointer,
        dummy
    ]

def interpret_mutex_give_failed_event(event):
    event_check(PSF_EVENT.MUTEX_GIVE_FAILED, event, 1)

    mutex_pointer = event[4]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{mutex_pointer:X}"
    ]

def interpret_mutex_give_block_event(event):
    event_check(PSF_EVENT.MUTEX_GIVE_BLOCK, event, 1)

    mutex_pointer = event[4]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{mutex_pointer:X}"
    ]

def interpret_mutex_peek_event(event):
    event_check(PSF_EVENT.MUTEX_PEEK, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    mutex_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]

    return [
        timestamp,
        event_type,
        mutex_pointer,
        ticks_to_wait
    ]

def interpret_mutex_take_event(event):
    event_check(PSF_EVENT.MUTEX_TAKE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    mutex_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]

    return [
        timestamp,
        event_type,
        mutex_pointer,
        ticks_to_wait
    ]

def interpret_mutex_take_recursive_event(event):
    event_check(PSF_EVENT.MUTEX_TAKE_RECURSIVE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    mutex_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]

    return [
        timestamp,
        event_type,
        mutex_pointer,
        ticks_to_wait
    ]

def interpret_mutex_peek_failed_event(event):
    event_check(PSF_EVENT.MUTEX_PEEK_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    mutex_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]

    return [
        timestamp,
        event_type,
        mutex_pointer,
        ticks_to_wait
    ]

def interpret_mutex_take_failed_event(event):
    event_check(PSF_EVENT.MUTEX_TAKE_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    mutex_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]

    return [
        timestamp,
        event_type,
        mutex_pointer,
        ticks_to_wait
    ]

def interpret_mutex_take_recursive_failed_event(event):
    event_check(PSF_EVENT.MUTEX_TAKE_RECURSIVE_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    mutex_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]

    return [
        timestamp,
        event_type,
        mutex_pointer,
        ticks_to_wait
    ]

def interpret_mutex_peek_block_event(event):
    event_check(PSF_EVENT.MUTEX_PEEK_BLOCK, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    mutex_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]

    return [
        timestamp,
        event_type,
        mutex_pointer,
        ticks_to_wait
    ]

def interpret_mutex_take_block_event(event):
    event_check(PSF_EVENT.MUTEX_TAKE_BLOCK, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    mutex_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]

    return [
        timestamp,
        event_type,
        mutex_pointer,
        ticks_to_wait
    ]

def interpret_mutex_take_recursive_block_event(event):
    event_check(PSF_EVENT.MUTEX_TAKE_RECURSIVE_BLOCK, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    mutex_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]

    return [
        timestamp,
        event_type,
        mutex_pointer,
        ticks_to_wait
    ]

def interpret_mutex_give_recursive_failed_event(event):
    event_check(PSF_EVENT.MUTEX_GIVE_RECURSIVE_FAILED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    mutex_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        mutex_pointer
    ]