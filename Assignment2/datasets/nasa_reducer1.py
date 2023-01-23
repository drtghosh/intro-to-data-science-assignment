import sys

current_id = None
activity = None
exec_id = None
current_starttime = 0
current_completetime = 0

for line in sys.stdin:
    exec_id, tuple3 = line.strip().split('\t', 1)
    activity, timestamp, life_transit = tuple3.split(',', 2)
    timestamp = float(timestamp)
    if current_id != exec_id:
        current_id = exec_id
        current_starttime = timestamp
    else:
        if life_transit == 'complete':
            current_completetime = timestamp
        else:
            current_completetime = current_starttime
            current_starttime = timestamp
        execution_time = current_completetime - current_starttime
        print(f"{activity}\t{execution_time}")
