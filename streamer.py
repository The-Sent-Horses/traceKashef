from decoder import psf_reader, PSF_DECODERS
from decoder.PSF_EVENTS import PSF_EVENT

import pyarrow as pa



schema = pa.schema([
    ("timestamp", pa.uint32()),
    ("event_type", pa.string()), 
    ("pointer", pa.uint32()),
    ("value", pa.uint32()), 
    ("name", pa.string()),

    
    
    ("handle_1", pa.uint32()),
    ("handle_2", pa.uint32()),
    
    ("arg1", pa.string()),
    ("arg2", pa.string()),
    ("arg3", pa.string()),
    ("arg4", pa.string()),
    ("func_hash", pa.uint64()), 
])

def extend_batch_array(base_batch_array, pointer=0, value=0, name="", handle_1=0, handle_2=0, args=None, func_hash=0):
    
    if args is None:
        args = [""] * 4
    
    base_batch_array[2] = pa.array([pointer])  # Pointer
    base_batch_array[3] = pa.array([value])  # Value
    base_batch_array[4] = pa.array([name])  # Name
    base_batch_array[5] = pa.array([handle_1])  # Handle 1
    base_batch_array[6] = pa.array([handle_2])  # Handle 2
    base_batch_array[7] = pa.array([args[0]])  # Arg1
    base_batch_array[8] = pa.array([args[1]])  # Arg2
    base_batch_array[9] = pa.array([args[2]])  # Arg3
    base_batch_array[10] = pa.array([args[3]])  # Arg4
    base_batch_array[11] = pa.array([func_hash])  # Function hash
    
    return base_batch_array

def handle_trace_start(base_batch_array, event):
    output_len = len(event[2:])
    if output_len == 1:
        return extend_batch_array(base_batch_array, pointer=event[2])
    elif output_len == 2:
        return extend_batch_array(base_batch_array, pointer=event[2], value=event[3])
    elif output_len == 3:
        return extend_batch_array(base_batch_array, pointer=event[2], value=event[3], args=[event[4], "", "", ""])
    elif output_len == 4:
        return extend_batch_array(base_batch_array, pointer=event[2], value=event[3], args=[event[4], event[5], "", ""])
    else:
        raise ValueError("Unexpected TRACE_START format")

DISPATCH_MAP = {
    PSF_EVENT.TASK_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], name=e[4]),
    PSF_EVENT.TASK_PRIORITY: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TASK_PRIO_INHERIT: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TASK_PRIO_DISINHERIT: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TASK_DELETE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TASK_READY: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.TASK_ACTIVATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.TASK_CREATE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TASK_DELAY_UNTIL: lambda e, base_batch_array: extend_batch_array(base_batch_array, value=e[2]),
    PSF_EVENT.TASK_SUSPEND: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.TASK_DELAY: lambda e, base_batch_array: extend_batch_array(base_batch_array, value=e[3]),
    PSF_EVENT.TASK_RESUME: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.TASK_RESUME_FROMISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.TASK_NOTIFY: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.TASK_NOTIFY_FROM_ISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.TASK_NOTIFY_WAIT_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TASK_NOTIFY_WAIT: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TASK_NOTIFY_WAIT_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], name=e[4]),
    PSF_EVENT.TIMER_RESET: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_RESET_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_START_FROMISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_START_FROMISR_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_RESET_FROMISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_RESET_FROMISR_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_STOP_FROMISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_STOP_FROMISR_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_CHANGEPERIOD_FROMISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_CHANGEPERIOD_FROMISR_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_START: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.TIMER_START_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.TIMER_STOP: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.TIMER_STOP_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.TIMER_CHANGEPERIOD: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_CHANGEPERIOD_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_EXPIRED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_DELETE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_CREATE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.TIMER_DELETE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.OBJ_NAME: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], name=e[3]),
    PSF_EVENT.TRACE_START: lambda e, base_batch_array: handle_trace_start(base_batch_array, e),
    PSF_EVENT.DEFINE_ISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], name=e[4]),
    PSF_EVENT.NEW_TIME: lambda e, base_batch_array: extend_batch_array(base_batch_array, value=e[2]),
    PSF_EVENT.NEW_TIME_SCHEDULER_SUSPENDED: lambda e, base_batch_array: extend_batch_array(base_batch_array, value=e[2]),
    PSF_EVENT.ISR_BEGIN: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.ISR_RESUME: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.TS_BEGIN: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.TS_RESUME: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.LOWPOWER_BEGIN: lambda e, base_batch_array: extend_batch_array(base_batch_array, value=e[2]),
    PSF_EVENT.LOWPOWER_END: lambda e, base_batch_array: extend_batch_array(base_batch_array, name="low_power_end"),
    PSF_EVENT.IFE_NEXT: lambda e, base_batch_array: extend_batch_array(base_batch_array, name="IFE_NEXT"),
    PSF_EVENT.IFE_DIRECT: lambda e, base_batch_array: extend_batch_array(base_batch_array, name="IFE_DIRECT"),
    PSF_EVENT.USER_EVENT_FIXED0: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.USER_EVENT_FIXED1: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], "", "", ""]),
    PSF_EVENT.USER_EVENT_FIXED2: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], e[5], "", ""]),
    PSF_EVENT.USER_EVENT_FIXED3: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], e[5], e[6], ""]),
    PSF_EVENT.USER_EVENT_FIXED4: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], e[5], e[6], e[7]]),
    PSF_EVENT.UNUSED_STACK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.STATEMACHINE_STATE_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, name=e[2], handle_1=e[3]),
    PSF_EVENT.STATEMACHINE_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.STATEMACHINE_STATECHANGE: lambda e, base_batch_array: extend_batch_array(base_batch_array, handle_1=e[2], handle_2=e[3]),
    PSF_EVENT.INTERVAL_CHANNEL_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, name=e[2], handle_1=e[3]),
    PSF_EVENT.INTERVAL_START: lambda e, base_batch_array: extend_batch_array(base_batch_array, handle_1=e[2], handle_2=e[3], value=e[4]),
    PSF_EVENT.EXTENSION_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, name=e[2], handle_1=e[3]),
    PSF_EVENT.HEAP_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, name=e[2]),
    PSF_EVENT.COUNTER_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, name=e[2]),
    PSF_EVENT.COUNTER_CHANGE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.COUNTER_LIMIT_EXCEEDED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),
    PSF_EVENT.INTERVAL_STOP: lambda e, base_batch_array: extend_batch_array(base_batch_array, handle_1=e[2], handle_2=e[3]),
    PSF_EVENT.INTERVAL_CHANNEL_SET_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, name=e[2]),
    PSF_EVENT.RUNNABLE_REGISTER: lambda e, base_batch_array: extend_batch_array(base_batch_array, handle_1=e[2], name=e[3]),
    PSF_EVENT.RUNNABLE_START: lambda e, base_batch_array: extend_batch_array(base_batch_array, handle_1=e[2]),
    PSF_EVENT.RUNNABLE_STOP: lambda e, base_batch_array: extend_batch_array(base_batch_array, handle_1=e[2], name="stopped"),
    PSF_EVENT.DEPENDENCY_REGISTER: lambda e, base_batch_array: extend_batch_array(base_batch_array, name=e[2]),
    PSF_EVENT.PEND_FUNC_CALL: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], func_hash=f"{e[3]} {e[4]}", args=[e[5], "", "", ""]),
    PSF_EVENT.PEND_FUNC_CALL_FROM_ISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], func_hash=e[3], args=[e[4], "", "", ""]),
    PSF_EVENT.PEND_FUNC_CALL_TRCFAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], func_hash=e[3], args=[e[4], "", "", ""]),
    PSF_EVENT.PEND_FUNC_CALL_FROM_ISR_TRCFAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], func_hash=e[3], args=[e[4], "", "", ""]),
    PSF_EVENT.SEMAPHORE_BINARY_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], name=e[4]),

    PSF_EVENT.SEMAPHORE_COUNTING_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], name=e[4]),

    PSF_EVENT.SEMAPHORE_DELETE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.SEMAPHORE_BINARY_CREATE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.SEMAPHORE_COUNTING_CREATE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.SEMAPHORE_GIVE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.SEMAPHORE_GIVE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.SEMAPHORE_GIVE_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.SEMAPHORE_GIVE_FROMISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.SEMAPHORE_GIVE_FROMISR_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.SEMAPHORE_PEEK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], "", "", ""]),

    PSF_EVENT.SEMAPHORE_TAKE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], "", "", ""]),

    PSF_EVENT.SEMAPHORE_PEEK_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], "", "", ""]),

    PSF_EVENT.SEMAPHORE_TAKE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], "", "", ""]),

    PSF_EVENT.SEMAPHORE_PEEK_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], "", "", ""]),

    PSF_EVENT.SEMAPHORE_TAKE_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], "", "", ""]),

    PSF_EVENT.SEMAPHORE_TAKE_FROMISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.SEMAPHORE_TAKE_FROMISR_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    PSF_EVENT.QUEUE_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], name=e[4]),

    PSF_EVENT.QUEUE_DELETE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.QUEUE_CREATE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.QUEUE_SEND: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.QUEUE_SEND_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.QUEUE_SEND_FRONT_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.QUEUE_SEND_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.QUEUE_SEND_FROMISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.QUEUE_SEND_FRONT_FROMISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.QUEUE_SEND_FROMISR_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.QUEUE_SEND_FRONT_FROMISR_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.QUEUE_PEEK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], "", "", ""]),

    PSF_EVENT.QUEUE_RECEIVE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], "", "", ""]),

    PSF_EVENT.QUEUE_PEEK_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], "", "", ""]),

    PSF_EVENT.QUEUE_RECEIVE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], "", "", ""]),

    PSF_EVENT.QUEUE_PEEK_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], "", "", ""]),

    PSF_EVENT.QUEUE_RECEIVE_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], args=[e[4], "", "", ""]),

    PSF_EVENT.QUEUE_RECEIVE_FROMISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.QUEUE_RECEIVE_FROMISR_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.QUEUE_SEND_FRONT: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.QUEUE_SEND_FRONT_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MUTEX_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], name=e[4]),

    PSF_EVENT.MUTEX_RECURSIVE_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], name=e[4]),

    PSF_EVENT.MUTEX_DELETE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MUTEX_GIVE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.MUTEX_GIVE_RECURSIVE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.MUTEX_CREATE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MUTEX_RECURSIVE_CREATE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MUTEX_GIVE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.MUTEX_GIVE_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.MUTEX_PEEK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MUTEX_TAKE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MUTEX_TAKE_RECURSIVE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MUTEX_PEEK_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MUTEX_TAKE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MUTEX_TAKE_RECURSIVE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MUTEX_PEEK_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MUTEX_TAKE_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MUTEX_TAKE_RECURSIVE_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MUTEX_GIVE_RECURSIVE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.MESSAGEBUFFER_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], name=e[4]),

    PSF_EVENT.STREAMBUFFER_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3], name=e[4]),

    PSF_EVENT.STREAMBUFFER_SEND: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.STREAMBUFFER_RESET: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.STREAMBUFFER_SEND_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.STREAMBUFFER_SEND_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.STREAMBUFFER_RECEIVE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.STREAMBUFFER_RECEIVE_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.STREAMBUFFER_RECEIVE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.STREAMBUFFER_SEND_FROM_ISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.STREAMBUFFER_SEND_FROM_ISR_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.STREAMBUFFER_RECEIVE_FROM_ISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.STREAMBUFFER_RECEIVE_FROM_ISR_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.MESSAGEBUFFER_SEND: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MESSAGEBUFFER_RESET: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MESSAGEBUFFER_SEND_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.MESSAGEBUFFER_SEND_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.MESSAGEBUFFER_RECEIVE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MESSAGEBUFFER_RECEIVE_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.MESSAGEBUFFER_RECEIVE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.MESSAGEBUFFER_SEND_FROM_ISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MESSAGEBUFFER_SEND_FROM_ISR_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.MESSAGEBUFFER_RECEIVE_FROM_ISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MESSAGEBUFFER_RECEIVE_FROM_ISR_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2]),

    PSF_EVENT.STREAMBUFFER_DELETE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MESSAGEBUFFER_DELETE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.STREAMBUFFER_CREATE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MESSAGEBUFFER_CREATE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.FREE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.FREE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MALLOC: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.MALLOC_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),
    
    PSF_EVENT.EVENTGROUP_CREATE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.EVENTGROUP_SYNC_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.EVENTGROUP_SYNC: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.EVENTGROUP_SYNC_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.EVENTGROUP_WAITBITS_BLOCK: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.EVENTGROUP_WAITBITS: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.EVENTGROUP_WAITBITS_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.EVENTGROUP_CLEARBITS: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.EVENTGROUP_CLEARBITS_FROMISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.EVENTGROUP_SETBITS: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.EVENTGROUP_SETBITS_FROMISR: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.EVENTGROUP_DELETE: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),

    PSF_EVENT.EVENTGROUP_CREATE_FAILED: lambda e, base_batch_array: extend_batch_array(base_batch_array, pointer=e[2], value=e[3]),


    }
class Streamer:
    traceKashef: psf_reader.psf_reader = None
    
    
    def __init__(self, traceKashef: psf_reader.psf_reader, perspective_table=None):
        self.traceKashef = traceKashef
        self.perspective_table = perspective_table
        self.clients = set()
        self.sink = None
        self.writer = None
    
    def get_event(self):

        try: 
            event = next(self.traceKashef)
            psf_event = event[1]
        except StopIteration:
            print("End of iterator reached.")
            return None, None
        
        try:
        
            decoder_function = PSF_DECODERS[psf_event]
            decoded_event = decoder_function(event)
            return decoded_event, psf_event
        except KeyError:
            print(f"Event 0x{psf_event:X} not found in PSF_DECODERS.")
            return None, None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None, None
    
    def create_batch_array(self):
        event, event_type = self.get_event()
        if event is None:
            return None
        base_batch_array = [
            pa.array([event[0]]),  # Timestamp
            pa.array([PSF_EVENT(event_type).name]),  # Event type
            pa.array([0]),  # Pointer
            pa.array([0]),  # Value
            pa.array([""]),  # Name
            pa.array([0]),  # Handle 1
            pa.array([0]),  # Handle 2
            pa.array([""]),  # Arg1
            pa.array([""]),  # Arg2
            pa.array([""]),  # Arg3
            pa.array([""]),  # Arg4
            pa.array([0]),  # Function hash
        ]
        handler = DISPATCH_MAP.get(event_type)
        if handler:
            base_batch_array = handler(event, base_batch_array)
        else:
            raise ValueError(f"Unsupported event_type: {event_type}")
        return pa.Table.from_arrays(base_batch_array, schema=schema)
    
    
    async def send_data(self):
        while True:
            self.create_sink_writer()
            batch = self.create_batch_array()
            
            if batch is None:
                self.writer.close()
                continue
            
            if self.perspective_table:
                self.perspective_table.update(batch.to_pydict())
                
    
    
            
            
            

        
    
    
        
        
        
    
    