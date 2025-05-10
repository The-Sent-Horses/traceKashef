from .common import event_check, extract_name_from_words
from .PSF_EVENTS import PSF_EVENT

def interpret_queue_create_event(event):
    event_check(PSF_EVENT.QUEUE_CREATE, event, 3)
    params = event[4:]
    queue_pointer = params[0]
    queue_length = params[1]
    name_words = params[2:]

    name = extract_name_from_words(name_words)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{queue_pointer:X}",
        queue_length,
        name
    ]

def interpret_queue_delete_event(event):
    event_check(PSF_EVENT.QUEUE_DELETE, event, 2)

    params = event[4:]
    queue_pointer = params[0]
    messages_waiting = params[1]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{queue_pointer:X}",
        messages_waiting
    ]

def interpret_queue_create_failed_event(event):
    event_check(PSF_EVENT.QUEUE_CREATE_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    queue_length = event[5]

    return [
        timestamp,
        event_type,
        queue_pointer,
        queue_length
    ]

def interpret_queue_send_event(event):
    event_check(PSF_EVENT.QUEUE_SEND, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    messages_waiting = event[5]

    return [
        timestamp,
        event_type,
        queue_pointer,
        messages_waiting
    ]

def interpret_queue_send_failed_event(event):
    event_check(PSF_EVENT.QUEUE_SEND_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    messages_waiting = event[5]

    return [
        timestamp,
        event_type,
        queue_pointer,
        messages_waiting
    ]

def interpret_queue_send_front_failed_event(event):
    event_check(PSF_EVENT.QUEUE_SEND_FRONT_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    messages_waiting = event[5]

    return [
        timestamp,
        event_type,
        queue_pointer,
        messages_waiting
    ]

def interpret_queue_send_block_event(event):
    event_check(PSF_EVENT.QUEUE_SEND_BLOCK, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    messages_waiting = event[5]

    return [
        timestamp,
        event_type,
        queue_pointer,
        messages_waiting
    ]

def interpret_queue_send_fromisr_event(event):
    event_check(PSF_EVENT.QUEUE_SEND_FROMISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    messages_after_send = event[5]

    return [
        timestamp,
        event_type,
        queue_pointer,
        messages_after_send
    ]

def interpret_queue_send_front_fromisr_event(event):
    event_check(PSF_EVENT.QUEUE_SEND_FRONT_FROMISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    messages_after_send = event[5]

    return [
        timestamp,
        event_type,
        queue_pointer,
        messages_after_send
    ]

def interpret_queue_send_fromisr_failed_event(event):
    event_check(PSF_EVENT.QUEUE_SEND_FROMISR_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    messages_waiting = event[5]

    return [
        timestamp,
        event_type,
        queue_pointer,
        messages_waiting
    ]

def interpret_queue_send_front_fromisr_failed_event(event):
    event_check(PSF_EVENT.QUEUE_SEND_FRONT_FROMISR_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    messages_waiting = event[5]

    return [
        timestamp,
        event_type,
        queue_pointer,
        messages_waiting
    ]

def interpret_queue_peek_event(event):
    event_check(PSF_EVENT.QUEUE_PEEK, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]
    messages_after_peek = event[6]

    return [
        timestamp,
        event_type,
        queue_pointer,
        ticks_to_wait,
        messages_after_peek
    ]

def interpret_queue_receive_event(event):
    event_check(PSF_EVENT.QUEUE_RECEIVE, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]
    messages_after_receive = event[6]

    return [
        timestamp,
        event_type,
        queue_pointer,
        ticks_to_wait,
        messages_after_receive
    ]

def interpret_queue_peek_failed_event(event):
    event_check(PSF_EVENT.QUEUE_PEEK_FAILED, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]
    messages_waiting = event[6]

    return [
        timestamp,
        event_type,
        queue_pointer,
        ticks_to_wait,
        messages_waiting
    ]

def interpret_queue_receive_failed_event(event):
    event_check(PSF_EVENT.QUEUE_RECEIVE_FAILED, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]
    messages_waiting = event[6]

    return [
        timestamp,
        event_type,
        queue_pointer,
        ticks_to_wait,
        messages_waiting
    ]

def interpret_queue_peek_block_event(event):
    event_check(PSF_EVENT.QUEUE_PEEK_BLOCK, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]
    messages_waiting = event[6]

    return [
        timestamp,
        event_type,
        queue_pointer,
        ticks_to_wait,
        messages_waiting
    ]

def interpret_queue_receive_block_event(event):
    event_check(PSF_EVENT.QUEUE_RECEIVE_BLOCK, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]
    messages_waiting = event[6]

    return [
        timestamp,
        event_type,
        queue_pointer,
        ticks_to_wait,
        messages_waiting
    ]

def interpret_queue_receive_fromisr_event(event):
    event_check(PSF_EVENT.QUEUE_RECEIVE_FROMISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    messages_after_receive = event[5]

    return [
        timestamp,
        event_type,
        queue_pointer,
        messages_after_receive
    ]

def interpret_queue_receive_fromisr_failed_event(event):
    event_check(PSF_EVENT.QUEUE_RECEIVE_FROMISR_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    messages_waiting = event[5]

    return [
        timestamp,
        event_type,
        queue_pointer,
        messages_waiting
    ]

def interpret_queue_send_front_event(event):
    event_check(PSF_EVENT.QUEUE_SEND_FRONT, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    messages_after_send = event[5]

    return [
        timestamp,
        event_type,
        queue_pointer,
        messages_after_send
    ]

def interpret_queue_send_front_block_event(event):
    event_check(PSF_EVENT.QUEUE_SEND_FRONT_BLOCK, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    queue_pointer = f"0x{event[4]:X}"
    messages_waiting = event[5]

    return [
        timestamp,
        event_type,
        queue_pointer,
        messages_waiting
    ]