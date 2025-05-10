from .common import event_check, extract_name_from_words
from .PSF_EVENTS import PSF_EVENT

def interpret_semaphore_binary_create_event(event):
    event_check(PSF_EVENT.SEMAPHORE_BINARY_CREATE, event, 3)
    params = event[4:]
    semaphore_pointer = params[0]
    dummy = params[1]
    name_words = params[2:]

    name = extract_name_from_words(name_words)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{semaphore_pointer:X}",
        dummy,
        name
    ]

def interpret_semaphore_counting_create_event(event):
    event_check(PSF_EVENT.SEMAPHORE_COUNTING_CREATE, event, 3)
    params = event[4:]
    semaphore_pointer = params[0]
    max_or_initial_count = params[1]
    name_words = params[2:]

    name = extract_name_from_words(name_words)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{semaphore_pointer:X}",
        max_or_initial_count,
        name
    ]

def interpret_semaphore_delete_event(event):
    event_check(PSF_EVENT.SEMAPHORE_DELETE, event, 2)

    params = event[4:]
    semaphore_pointer = params[0]
    messages_waiting = params[1]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{semaphore_pointer:X}",
        messages_waiting
    ]

def interpret_semaphore_binary_create_failed_event(event):
    event_check(PSF_EVENT.SEMAPHORE_BINARY_CREATE_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    semaphore_pointer = f"0x{event[4]:X}"
    dummy = event[5]

    return [
        timestamp,
        event_type,
        semaphore_pointer,
        dummy
    ]

def interpret_semaphore_counting_create_failed_event(event):
    event_check(PSF_EVENT.SEMAPHORE_COUNTING_CREATE_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    semaphore_pointer = f"0x{event[4]:X}"
    max_or_init_count = event[5]

    return [
        timestamp,
        event_type,
        semaphore_pointer,
        max_or_init_count
    ]

def interpret_semaphore_give_event(event):
    event_check(PSF_EVENT.SEMAPHORE_GIVE, event, 2)

    semaphore_pointer = event[4]
    messages_after_give = event[5]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{semaphore_pointer:X}",
        messages_after_give
    ]

def interpret_semaphore_give_failed_event(event):
    event_check(PSF_EVENT.SEMAPHORE_GIVE_FAILED, event, 2)

    semaphore_pointer = event[4]
    messages_waiting = event[5]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{semaphore_pointer:X}",
        messages_waiting
    ]

def interpret_semaphore_give_block_event(event):
    event_check(PSF_EVENT.SEMAPHORE_GIVE_BLOCK, event, 2)

    semaphore_pointer = event[4]
    messages_waiting = event[5]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{semaphore_pointer:X}",
        messages_waiting
    ]

def interpret_semaphore_give_fromisr_event(event):
    event_check(PSF_EVENT.SEMAPHORE_GIVE_FROMISR, event, 2)

    semaphore_pointer = event[4]
    messages_after_give = event[5]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{semaphore_pointer:X}",
        messages_after_give
    ]

def interpret_semaphore_give_fromisr_failed_event(event):
    event_check(PSF_EVENT.SEMAPHORE_GIVE_FROMISR_FAILED, event, 2)

    semaphore_pointer = event[4]
    messages_waiting = event[5]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{semaphore_pointer:X}",
        messages_waiting
    ]

def interpret_semaphore_peek_event(event):
    event_check(PSF_EVENT.SEMAPHORE_PEEK, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    semaphore_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]
    messages_after = event[6]

    return [
        timestamp,
        event_type,
        semaphore_pointer,
        ticks_to_wait,
        messages_after
    ]

def interpret_semaphore_take_event(event):
    event_check(PSF_EVENT.SEMAPHORE_TAKE, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    semaphore_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]
    messages_after = event[6]

    return [
        timestamp,
        event_type,
        semaphore_pointer,
        ticks_to_wait,
        messages_after
    ]

def interpret_semaphore_peek_failed_event(event):
    event_check(PSF_EVENT.SEMAPHORE_PEEK_FAILED, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    semaphore_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]
    messages_waiting = event[6]

    return [
        timestamp,
        event_type,
        semaphore_pointer,
        ticks_to_wait,
        messages_waiting
    ]

def interpret_semaphore_take_failed_event(event):
    event_check(PSF_EVENT.SEMAPHORE_TAKE_FAILED, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    semaphore_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]
    messages_waiting = event[6]

    return [
        timestamp,
        event_type,
        semaphore_pointer,
        ticks_to_wait,
        messages_waiting
    ]

def interpret_semaphore_peek_block_event(event):
    event_check(PSF_EVENT.SEMAPHORE_PEEK_BLOCK, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    semaphore_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]
    messages_waiting = event[6]

    return [
        timestamp,
        event_type,
        semaphore_pointer,
        ticks_to_wait,
        messages_waiting
    ]

def interpret_semaphore_take_block_event(event):
    event_check(PSF_EVENT.SEMAPHORE_TAKE_BLOCK, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    semaphore_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]
    messages_waiting = event[6]

    return [
        timestamp,
        event_type,
        semaphore_pointer,
        ticks_to_wait,
        messages_waiting
    ]

def interpret_semaphore_take_fromisr_event(event):
    event_check(PSF_EVENT.SEMAPHORE_TAKE_FROMISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    semaphore_pointer = f"0x{event[4]:X}"
    messages_after = event[5]

    return [
        timestamp,
        event_type,
        semaphore_pointer,
        messages_after
    ]

def interpret_semaphore_take_fromisr_failed_event(event):
    event_check(PSF_EVENT.SEMAPHORE_TAKE_FROMISR_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    semaphore_pointer = f"0x{event[4]:X}"
    messages_waiting = event[5]

    return [
        timestamp,
        event_type,
        semaphore_pointer,
        messages_waiting
    ]