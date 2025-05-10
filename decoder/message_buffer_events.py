from .common import event_check, extract_name_from_words
from .PSF_EVENTS import PSF_EVENT

def interpret_messagebuffer_create_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_CREATE, event, 3)

    params = event[4:]
    messagebuffer_pointer = params[0]
    buffer_size = params[1]
    name_words = params[2:]

    name = extract_name_from_words(name_words)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{messagebuffer_pointer:X}",
        buffer_size,
        name
    ]

def interpret_streambuffer_create_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_CREATE, event, 3)

    params = event[4:]
    streambuffer_pointer = params[0]
    buffer_size = params[1]
    name_words = params[2:]

    name = extract_name_from_words(name_words)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{streambuffer_pointer:X}",
        buffer_size,
        name
    ]

def interpret_streambuffer_send_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_SEND, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    streambuffer_pointer = f"0x{event[4]:X}"
    bytes_in_buffer = event[5]

    return [
        timestamp,
        event_type,
        streambuffer_pointer,
        bytes_in_buffer
    ]

def interpret_streambuffer_reset_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_RESET, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    streambuffer_pointer = f"0x{event[4]:X}"
    dummy = event[5]

    return [
        timestamp,
        event_type,
        streambuffer_pointer,
        dummy
    ]

def interpret_streambuffer_send_block_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_SEND_BLOCK, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    streambuffer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        streambuffer_pointer
    ]

def interpret_streambuffer_send_failed_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_SEND_FAILED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    streambuffer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        streambuffer_pointer
    ]

def interpret_streambuffer_receive_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_RECEIVE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    streambuffer_pointer = f"0x{event[4]:X}"
    bytes_in_buffer = event[5]

    return [
        timestamp,
        event_type,
        streambuffer_pointer,
        bytes_in_buffer
    ]

def interpret_streambuffer_receive_block_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_RECEIVE_BLOCK, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    streambuffer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        streambuffer_pointer
    ]

def interpret_streambuffer_receive_failed_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_RECEIVE_FAILED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    streambuffer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        streambuffer_pointer
    ]

def interpret_streambuffer_send_from_isr_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_SEND_FROM_ISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    streambuffer_pointer = f"0x{event[4]:X}"
    bytes_in_buffer = event[5]

    return [
        timestamp,
        event_type,
        streambuffer_pointer,
        bytes_in_buffer
    ]

def interpret_streambuffer_send_from_isr_failed_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_SEND_FROM_ISR_FAILED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    streambuffer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        streambuffer_pointer
    ]

def interpret_streambuffer_receive_from_isr_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_RECEIVE_FROM_ISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    streambuffer_pointer = f"0x{event[4]:X}"
    bytes_in_buffer = event[5]

    return [
        timestamp,
        event_type,
        streambuffer_pointer,
        bytes_in_buffer
    ]

def interpret_streambuffer_receive_from_isr_failed_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_RECEIVE_FROM_ISR_FAILED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    streambuffer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        streambuffer_pointer
    ]

def interpret_messagebuffer_send_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_SEND, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    messagebuffer_pointer = f"0x{event[4]:X}"
    bytes_in_buffer = event[5]

    return [
        timestamp,
        event_type,
        messagebuffer_pointer,
        bytes_in_buffer
    ]

def interpret_messagebuffer_reset_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_RESET, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    messagebuffer_pointer = f"0x{event[4]:X}"
    dummy = event[5]

    return [
        timestamp,
        event_type,
        messagebuffer_pointer,
        dummy
    ]

def interpret_messagebuffer_send_block_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_SEND_BLOCK, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    messagebuffer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        messagebuffer_pointer
    ]

def interpret_messagebuffer_send_failed_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_SEND_FAILED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    messagebuffer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        messagebuffer_pointer
    ]

def interpret_messagebuffer_receive_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_RECEIVE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    messagebuffer_pointer = f"0x{event[4]:X}"
    bytes_in_buffer = event[5]

    return [
        timestamp,
        event_type,
        messagebuffer_pointer,
        bytes_in_buffer
    ]

def interpret_messagebuffer_receive_block_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_RECEIVE_BLOCK, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    messagebuffer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        messagebuffer_pointer
    ]

def interpret_messagebuffer_receive_failed_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_RECEIVE_FAILED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    messagebuffer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        messagebuffer_pointer
    ]

def interpret_messagebuffer_send_from_isr_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_SEND_FROM_ISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    messagebuffer_pointer = f"0x{event[4]:X}"
    bytes_in_buffer = event[5]

    return [
        timestamp,
        event_type,
        messagebuffer_pointer,
        bytes_in_buffer
    ]

def interpret_messagebuffer_send_from_isr_failed_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_SEND_FROM_ISR_FAILED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    messagebuffer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        messagebuffer_pointer
    ]

def interpret_messagebuffer_receive_from_isr_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_RECEIVE_FROM_ISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    messagebuffer_pointer = f"0x{event[4]:X}"
    bytes_in_buffer = event[5]

    return [
        timestamp,
        event_type,
        messagebuffer_pointer,
        bytes_in_buffer
    ]

def interpret_messagebuffer_receive_from_isr_failed_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_RECEIVE_FROM_ISR_FAILED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    messagebuffer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        messagebuffer_pointer
    ]

def interpret_streambuffer_delete_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_DELETE, event, 2)

    params = event[4:]
    streambuffer_pointer = params[0]
    bytes_in_buffer = params[1]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{streambuffer_pointer:X}",
        bytes_in_buffer
    ]

def interpret_messagebuffer_delete_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_DELETE, event, 2)

    params = event[4:]
    messagebuffer_pointer = params[0]
    bytes_in_buffer = params[1]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{messagebuffer_pointer:X}",
        bytes_in_buffer
    ]

def interpret_streambuffer_create_failed_event(event):
    event_check(PSF_EVENT.STREAMBUFFER_CREATE_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    pointer = f"0x{event[4]:X}"
    buffer_size = event[5]

    return [
        timestamp,
        event_type,
        pointer,
        buffer_size
    ]

def interpret_messagebuffer_create_failed_event(event):
    event_check(PSF_EVENT.MESSAGEBUFFER_CREATE_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    pointer = f"0x{event[4]:X}"
    buffer_size = event[5]

    return [
        timestamp,
        event_type,
        pointer,
        buffer_size
    ]