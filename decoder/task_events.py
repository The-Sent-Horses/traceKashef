from .common import event_check, extract_name_from_words
from .PSF_EVENTS import PSF_EVENT

def interpret_task_create_event(event):
    event_check(PSF_EVENT.TASK_CREATE, event, 3)
    params = event[4:]
    task_pointer = params[0]
    priority = params[1]
    name_words = params[2:]

    name = extract_name_from_words(name_words)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{task_pointer:X}",
        priority,
        name
    ]

def interpret_task_priority_event(event):
    event_check(PSF_EVENT.TASK_PRIORITY, event, 2)

    params = event[4:]
    task_pointer, priority = params

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{task_pointer:X}",
        priority
    ]

def interpret_task_prio_inherit_event(event):
    event_check(PSF_EVENT.TASK_PRIO_INHERIT, event, 2)

    params = event[4:]
    task_pointer, new_priority = params

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{task_pointer:X}",
        new_priority
    ]

def interpret_task_prio_disinherit_event(event):
    event_check(PSF_EVENT.TASK_PRIO_DISINHERIT, event, 2)

    params = event[4:]
    task_pointer, restored_priority = params

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{task_pointer:X}",
        restored_priority
    ]

def interpret_task_delete_event(event):
    event_check(PSF_EVENT.TASK_DELETE, event, 2)

    params = event[4:]
    task_pointer = params[0]
    priority = params[1]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{task_pointer:X}",
        priority
    ]

def interpret_task_ready_event(event):
    event_check(PSF_EVENT.TASK_READY, event, 1)

    task_pointer = event[4]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{task_pointer:X}"
    ]

def interpret_task_activate_event(event):
    event_check(PSF_EVENT.TASK_ACTIVATE, event, 1)

    task_pointer = event[4]

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name

    return [
        timestamp,
        event_type,
        f"0x{task_pointer:X}"
    ]

def interpret_task_create_failed_event(event):
    event_check(PSF_EVENT.TASK_CREATE_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    task_pointer = f"0x{event[4]:X}"
    priority_or_info = event[5]

    return [
        timestamp,
        event_type,
        task_pointer,
        priority_or_info
    ]

def interpret_task_delay_until_event(event):
    event_check(PSF_EVENT.TASK_DELAY_UNTIL, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    time_to_wake = event[4]

    return [
        timestamp,
        event_type,
        time_to_wake
    ]

def interpret_task_suspend_event(event):
    event_check(PSF_EVENT.TASK_SUSPEND, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    task_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        task_pointer
    ]

def interpret_task_delay_event(event):
    event_check(PSF_EVENT.TASK_DELAY, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    ticks_to_delay = event[4]

    return [
        timestamp,
        event_type,
        "0x0000",  # Not used
        ticks_to_delay
    ]

def interpret_task_resume_event(event):
    event_check(PSF_EVENT.TASK_RESUME, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    task_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        task_pointer
    ]

def interpret_task_resume_fromisr_event(event):
    event_check(PSF_EVENT.TASK_RESUME_FROMISR, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    task_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        task_pointer
    ]

def interpret_task_notify_event(event):
    event_check(PSF_EVENT.TASK_NOTIFY, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    task_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        task_pointer
    ]

def interpret_task_notify_fromisr_event(event):
    event_check(PSF_EVENT.TASK_NOTIFY_FROM_ISR, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    task_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        task_pointer
    ]

def interpret_task_notify_wait_block_event(event):
    event_check(PSF_EVENT.TASK_NOTIFY_WAIT_BLOCK, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    task_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]

    return [
        timestamp,
        event_type,
        task_pointer,
        ticks_to_wait
    ]

def interpret_task_notify_wait_event(event):
    event_check(PSF_EVENT.TASK_NOTIFY_WAIT, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    task_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]

    return [
        timestamp,
        event_type,
        task_pointer,
        ticks_to_wait
    ]

def interpret_task_notify_wait_failed_event(event):
    event_check(PSF_EVENT.TASK_NOTIFY_WAIT_FAILED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    task_pointer = f"0x{event[4]:X}"
    ticks_to_wait = event[5]

    return [
        timestamp,
        event_type,
        task_pointer,
        ticks_to_wait
    ]