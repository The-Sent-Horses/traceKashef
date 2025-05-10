from .common import event_check, extract_name_from_words
from .PSF_EVENTS import PSF_EVENT

def interpret_obj_name_event(event):
    event_check(PSF_EVENT.OBJ_NAME, event, 3)
    # Parameters start from index 4 onward
    timestamp = event[3]
    
    params = event[4:]

    object_pointer = params[0]
    
    name= extract_name_from_words(params[1:])

    return [
        event[3],
        PSF_EVENT(event[1]).name,
        f"0x{object_pointer:X}",
        name
    ]
    
    
def interpret_trace_start_event(event):
    event_check(PSF_EVENT.TRACE_START, event, 5)
    timestamp = event[3]
    task_pointers = event[4:]  # parameters start after timestamp
    
    
    output = [
        timestamp,
        PSF_EVENT(event[1]).name,
    ]
    
    for i in (task_pointers):
        output.append(f"0x{i:X}")

    return output

def interpret_define_isr_event(event):
    event_check(PSF_EVENT.DEFINE_ISR, event, 3)
    timestamp = event[3]

    params = event[4:]
    xEntryHandle = params[0]
    priority = params[1]
    name_words = params[2:]

    # Convert packed ASCII to string
    name_bytes = []
    for word in name_words:
        name_bytes.extend(word.to_bytes(4, byteorder='little'))
    name = bytes(name_bytes).split(b'\x00')[0].decode('ascii', errors='replace')

    
    return [
        timestamp,
        PSF_EVENT(event[1]).name,
        f"0x{xEntryHandle:X}",
        priority,
        name
    ]

def interpret_new_time_event(event):
    event_check(PSF_EVENT.NEW_TIME, event, 1)

    timestamp = event[3]
    tick_count = event[4]

    # return [
    #     timestamp,
    #     PSF_EVENT(event[1]).name,
    #     tick_count
    # ]
    return None # tempurary to avoid spam


def interpret_new_time_scheduler_suspended_event(event):
    event_check(PSF_EVENT.NEW_TIME_SCHEDULER_SUSPENDED, event, 1)
    timestamp = event[3]
    tick_count = event[4]

    return [
        timestamp,
        PSF_EVENT(event[1]).name,
        tick_count
    ]
    
def interpret_isr_begin_event(event):
    
    event_check(PSF_EVENT.ISR_BEGIN, event, 1)
    # Parameters start from index 4 onward
    timestamp = event[3]
    isr_pointer = event[4]

    return [
        timestamp,
        PSF_EVENT(event[1]).name,
        f"0x{isr_pointer:X}"
    ]

def interpret_isr_resume_event(event):
    event_check(PSF_EVENT.ISR_RESUME, event, 1)

    timestamp = event[3]
    isr_pointer = event[4]

    return [
        timestamp,
        PSF_EVENT(event[1]).name,
        f"0x{isr_pointer:X}"
    ]

def interpret_ts_begin_event(event):
    event_check(PSF_EVENT.TS_BEGIN, event, 1)

    timestamp = event[3]
    task_pointer = event[4]

    return [
        timestamp,
        PSF_EVENT(event[1]).name,
        f"0x{task_pointer:X}"
    ]

def interpret_ts_resume_event(event):
    
    event_check(PSF_EVENT.TS_RESUME, event, 1)
    timestamp = event[3]

    task_pointer = event[4]

    return [
        timestamp,
        PSF_EVENT(event[1]).name,
        f"0x{task_pointer:X}"
    ]
    
           
def interpret_lowpower_begin_event(event):
    event_check(PSF_EVENT.LOWPOWER_BEGIN, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    expected_idle_time = event[4]

    return [
        timestamp,
        event_type,
        expected_idle_time
    ]

def interpret_lowpower_end_event(event):
    event_check(PSF_EVENT.LOWPOWER_END, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    state = "low_power_end"

    return [
        timestamp,
        event_type,
        state
    ]

def interpret_ife_next_event(event):
    event_check(PSF_EVENT.IFE_NEXT, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    ife_next = "IFE_NEXT"

    return [
        timestamp,
        event_type,
        ife_next
    ]

def interpret_ife_direct_event(event):
    event_check(PSF_EVENT.IFE_DIRECT, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    ife_direct = "IFE_DIRECT"

    return [
        timestamp,
        event_type,
        ife_direct
    ]

def interpret_user_event_fixed_0(event):
    event_check(PSF_EVENT.USER_EVENT_FIXED, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    channel_pointer = f"0x{event[4]:X}"
    format_pointer = f"0x{event[5]:X}"

    return [
        timestamp,
        event_type,
        channel_pointer,
        format_pointer
    ]

def interpret_user_event_fixed_1(event):
    event_check(PSF_EVENT.USER_EVENT_FIXED + 1, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    channel_pointer = f"0x{event[4]:X}"
    format_pointer = f"0x{event[5]:X}"
    arg1 = event[6]

    return [
        timestamp,
        event_type,
        channel_pointer,
        format_pointer,
        arg1
    ]

def interpret_user_event_fixed_2(event):
    event_check(PSF_EVENT.USER_EVENT_FIXED + 2, event, 4)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    channel_pointer = f"0x{event[4]:X}"
    format_pointer = f"0x{event[5]:X}"
    arg1 = event[6]
    arg2 = event[7]

    return [
        timestamp,
        event_type,
        channel_pointer,
        format_pointer,
        arg1,
        arg2
    ]

def interpret_user_event_fixed_3(event):
    event_check(PSF_EVENT.USER_EVENT_FIXED + 3, event, 5)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    channel_pointer = f"0x{event[4]:X}"
    format_pointer = f"0x{event[5]:X}"
    arg1 = event[6]
    arg2 = event[7]
    arg3 = event[8]

    return [
        timestamp,
        event_type,
        channel_pointer,
        format_pointer,
        arg1,
        arg2,
        arg3
    ]

def interpret_user_event_fixed_4(event):
    event_check(PSF_EVENT.USER_EVENT_FIXED + 4, event, 6)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    channel_pointer = f"0x{event[4]:X}"
    format_pointer = f"0x{event[5]:X}"
    arg1 = event[6]
    arg2 = event[7]
    arg3 = event[8]
    arg4 = event[9]

    return [
        timestamp,
        event_type,
        channel_pointer,
        format_pointer,
        arg1,
        arg2,
        arg3,
        arg4
    ]






def interpret_unused_stack_event(event):
    event_check(PSF_EVENT.UNUSED_STACK, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    task_id = event[4]
    previous_low_watermark = event[5]

    return [
        timestamp,
        event_type,
        task_id,
        previous_low_watermark
    ]

def interpret_statemachine_state_create_event(event):
    event_check(PSF_EVENT.STATEMACHINE_STATE_CREATE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    name = extract_name_from_words(event[4])
    state_machine_handle = event[5]

    return [
        timestamp,
        event_type,
        name,
        state_machine_handle
    ]

def interpret_statemachine_create_event(event):
    event_check(PSF_EVENT.STATEMACHINE_CREATE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    name_pointer = f"0x{event[4]:X}"

    return [
        timestamp,
        event_type,
        name_pointer
    ]

def interpret_statemachine_statechange_event(event):
    event_check(PSF_EVENT.STATEMACHINE_STATECHANGE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    statemachine_handle = event[4]
    state_handle = event[5]

    return [
        timestamp,
        event_type,
        statemachine_handle,
        state_handle
    ]

def interpret_interval_channel_create_event(event):
    event_check(PSF_EVENT.INTERVAL_CHANNEL_CREATE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    name = extract_name_from_words(event[4])
    channel_set_handle = event[5]

    return [
        timestamp,
        event_type,
        name,
        channel_set_handle
    ]

def interpret_interval_start_event(event):
    event_check(PSF_EVENT.INTERVAL_START, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    channel_handle = event[4]
    instance_handle = event[5]
    value = event[6]

    return [
        timestamp,
        event_type,
        channel_handle,
        instance_handle,
        value
    ]

def interpret_extension_create_event(event):
    event_check(PSF_EVENT.EXTENSION_CREATE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    name = extract_name_from_words(event[4])
    dummy_or_state_count = event[5]

    return [
        timestamp,
        event_type,
        name,
        dummy_or_state_count
    ]

def interpret_heap_create_event(event):
    event_check(PSF_EVENT.HEAP_CREATE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    name = extract_name_from_words(event[4])

    return [
        timestamp,
        event_type,
        name
    ]

def interpret_counter_create_event(event):
    event_check(PSF_EVENT.COUNTER_CREATE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    name = extract_name_from_words(event[4])

    return [
        timestamp,
        event_type,
        name
    ]

def interpret_counter_change_event(event):
    event_check(PSF_EVENT.COUNTER_CHANGE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    counter_handle = event[4]
    value = event[5]

    return [
        timestamp,
        event_type,
        counter_handle,
        value
    ]

def interpret_counter_limit_exceeded_event(event):
    event_check(PSF_EVENT.COUNTER_LIMIT_EXCEEDED, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    counter_handle = event[4]

    return [
        timestamp,
        event_type,
        counter_handle
    ]

def interpret_interval_stop_event(event):
    event_check(PSF_EVENT.INTERVAL_STOP, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    channel_handle = event[4]
    instance_handle = event[5]

    return [
        timestamp,
        event_type,
        channel_handle,
        instance_handle
    ]

def interpret_interval_channel_set_create_event(event):
    event_check(PSF_EVENT.INTERVAL_CHANNEL_SET_CREATE, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    name = extract_name_from_words(event[4])

    return [
        timestamp,
        event_type,
        name
    ]

def interpret_runnable_register_event(event):
    event_check(PSF_EVENT.RUNNABLE_REGISTER, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    runnable_handle = event[4]
    name = extract_name_from_words(event[5])

    return [
        timestamp,
        event_type,
        runnable_handle,
        name
    ]

def interpret_runnable_start_event(event):
    event_check(PSF_EVENT.RUNNABLE_START, event, 1)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    runnable_handle = event[4]

    return [
        timestamp,
        event_type,
        runnable_handle
    ]

def interpret_runnable_stop_event(event):
    event_check(PSF_EVENT.RUNNABLE_STOP, event, 0)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    runnable_handle = event[4]
    status = "stopped"

    return [
        timestamp,
        event_type,
        runnable_handle,
        status
    ]

def interpret_dependency_register_event(event):
    event_check(PSF_EVENT.DEPENDENCY_REGISTER, event, 2)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    name = extract_name_from_words(event[4])

    return [
        timestamp,
        event_type,
        name
    ]

def interpret_pend_func_call_event(event):
    event_check(PSF_EVENT.PEND_FUNC_CALL, event, 4)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    daemon_task = f"0x{event[4]:X}"
    func_hash = f"{event[5]} {event[6]}"
    argument = f"0x{event[7]:X}"

    return [
        timestamp,
        event_type,
        daemon_task,
        func_hash,
        argument
    ]

def interpret_pend_func_call_from_isr_event(event):
    event_check(PSF_EVENT.PEND_FUNC_CALL_FROM_ISR, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    daemon_task = f"0x{event[4]:X}"
    func_hash = event[5]
    argument = f"0x{event[6]:X}"

    return [
        timestamp,
        event_type,
        daemon_task,
        func_hash,
        argument
    ]

def interpret_pend_func_call_trcfailed_event(event):
    event_check(PSF_EVENT.PEND_FUNC_CALL_TRCFAILED, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    daemon_task = f"0x{event[4]:X}"
    func_hash = event[5]
    argument = f"0x{event[6]:X}"

    return [
        timestamp,
        event_type,
        daemon_task,
        func_hash,
        argument
    ]

def interpret_pend_func_call_from_isr_trcfailed_event(event):
    event_check(PSF_EVENT.PEND_FUNC_CALL_FROM_ISR_TRCFAILED, event, 3)

    timestamp = event[3]
    event_type = PSF_EVENT(event[1]).name
    daemon_task = f"0x{event[4]:X}"
    func_hash = event[5]
    argument = f"0x{event[6]:X}"

    return [
        timestamp,
        event_type,
        daemon_task,
        func_hash,
        argument
    ]