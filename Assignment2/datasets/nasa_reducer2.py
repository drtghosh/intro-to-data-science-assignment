import sys

current_activity = None
current_totaltime = 0
current_freq = 1
mean_exec_time = 0

for line in sys.stdin:
    line = line.strip()
    activity, exec_time = line.split('\t', 1)
    exec_time = float(exec_time)
    if current_activity != activity:
        if current_activity is not None:
            mean_exec_time = current_totaltime/current_freq
            print("{}\t{}\t{}".format(current_activity, mean_exec_time, current_freq))
        current_activity = activity
        current_totaltime = exec_time
        current_freq = 1
    else:
        current_totaltime += exec_time
        current_freq += 1

if current_activity == activity:
    print("{}\t{}\t{}".format(current_activity, mean_exec_time, current_freq))
