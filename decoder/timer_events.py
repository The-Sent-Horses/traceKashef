from .common import event_check, extract_name_from_words
from .PSF_EVENTS import PSF_EVENT

def interpret_timer_create_event(event):
    event_check(PSF_EVENT.TIMER_CREATE, event, 3)
    params = event[4:]
    timer_pointer = params[0]
    period_ticks = params[1]
    name_words = params[2:]

    name = extract_name_from_words(name_words)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{timer_pointer:X}",
        period_ticks,
        name
    ]

def interpret_timer_pendfunccall_event(event):
    event_check(PSF_EVENT.TIMER_PENDFUNCCALL, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    function_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        function_pointer
    ]

def interpret_timer_pendfunccall_failed_event(event):
    event_check(PSF_EVENT.TIMER_PENDFUNCCALL_FAILED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    function_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        function_pointer
    ]

def interpret_timer_pendfunccall_fromisr_event(event):
    event_check(PSF_EVENT.TIMER_PENDFUNCCALL_FROMISR, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    function_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        function_pointer
    ]

def interpret_timer_pendfunccall_fromisr_failed_event(event):
    event_check(PSF_EVENT.TIMER_PENDFUNCCALL_FROMISR_FAILED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    function_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        function_pointer
    ]

def interpret_timer_reset_event(event):
    event_check(PSF_EVENT.TIMER_RESET, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    optional_value = event[5]

    return [
        timestamp,
        event_type,
        timer_pointer,
        optional_value
    ]

def interpret_timer_reset_failed_event(event):
    event_check(PSF_EVENT.TIMER_RESET_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    optional_value = event[5]

    return [
        timestamp,
        event_type,
        timer_pointer,
        optional_value
    ]

def interpret_timer_start_fromisr_event(event):
    event_check(PSF_EVENT.TIMER_START_FROMISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    optional_value = event[5]

    return [
        timestamp,
        event_type,
        timer_pointer,
        optional_value
    ]

def interpret_timer_start_fromisr_failed_event(event):
    event_check(PSF_EVENT.TIMER_START_FROMISR_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    optional_value = event[5]

    return [
        timestamp,
        event_type,
        timer_pointer,
        optional_value
    ]

def interpret_timer_reset_fromisr_event(event):
    event_check(PSF_EVENT.TIMER_RESET_FROMISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    optional_value = event[5]

    return [
        timestamp,
        event_type,
        timer_pointer,
        optional_value
    ]

def interpret_timer_reset_fromisr_failed_event(event):
    event_check(PSF_EVENT.TIMER_RESET_FROMISR_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    optional_value = event[5]

    return [
        timestamp,
        event_type,
        timer_pointer,
        optional_value
    ]

def interpret_timer_stop_fromisr_event(event):
    event_check(PSF_EVENT.TIMER_STOP_FROMISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    optional_value = event[5]

    return [
        timestamp,
        event_type,
        timer_pointer,
        optional_value
    ]

def interpret_timer_stop_fromisr_failed_event(event):
    event_check(PSF_EVENT.TIMER_STOP_FROMISR_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    optional_value = event[5]

    return [
        timestamp,
        event_type,
        timer_pointer,
        optional_value
    ]

def interpret_timer_changeperiod_fromisr_event(event):
    event_check(PSF_EVENT.TIMER_CHANGEPERIOD_FROMISR, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    optional_value = event[5]

    return [
        timestamp,
        event_type,
        timer_pointer,
        optional_value
    ]

def interpret_timer_changeperiod_fromisr_failed_event(event):
    event_check(PSF_EVENT.TIMER_CHANGEPERIOD_FROMISR_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    optional_value = event[5]

    return [
        timestamp,
        event_type,
        timer_pointer,
        optional_value
    ]

def interpret_timer_start_event(event):
    event_check(PSF_EVENT.TIMER_START, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        timer_pointer
    ]

def interpret_timer_start_failed_event(event):
    event_check(PSF_EVENT.TIMER_START_FAILED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        timer_pointer
    ]

def interpret_timer_stop_event(event):
    event_check(PSF_EVENT.TIMER_STOP, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        timer_pointer
    ]

def interpret_timer_stop_failed_event(event):
    event_check(PSF_EVENT.TIMER_STOP_FAILED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        timer_pointer
    ]

def interpret_timer_changeperiod_event(event):
    event_check(PSF_EVENT.TIMER_CHANGEPERIOD, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    optional_value = event[5]

    return [
        timestamp,
        event_type,
        timer_pointer,
        optional_value
    ]

def interpret_timer_changeperiod_failed_event(event):
    event_check(PSF_EVENT.TIMER_CHANGEPERIOD_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    optional_value = event[5]

    return [
        timestamp,
        event_type,
        timer_pointer,
        optional_value
    ]

def interpret_timer_expired_event(event):
    event_check(PSF_EVENT.TIMER_EXPIRED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    callback_pointer = f"0x{event[5]:X}"

    return [
        timestamp,
        event_type,
        timer_pointer,
        callback_pointer
    ]

def interpret_timer_delete_event(event):
    event_check(PSF_EVENT.TIMER_DELETE, event, 2)

    params = event[4:]
    timer_pointer = params[0]
    dummy = params[1]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{timer_pointer:X}",
        dummy
    ]

def interpret_timer_create_failed_event(event):
    event_check(PSF_EVENT.TIMER_CREATE_FAILED, event, 2)

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

def interpret_timer_delete_failed_event(event):
    event_check(PSF_EVENT.TIMER_DELETE_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    timer_pointer = f"0x{event[4]:X}"
    dummy = event[5]

    return [
        timestamp,
        event_type,
        timer_pointer,
        dummy
    ]