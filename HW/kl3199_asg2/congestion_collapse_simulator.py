import subprocess

# simulations for sliding window with different window size
# setting:   MIN_TIMEOUT = 100  MAX_TIMEOUT = 1000   seed=1, rtt_min=10, ticks=100000, queue_limit=10000
for i in range(1, 1001):
    if i % 10 == 1 or i == 1000:
        param1 = ["--seed", "1"]
        param2 = ["--host_type", "SlidingWindow"]
        param3 = ["--rtt_min", "10"]
        param4 = ["--ticks", "100000"]
        param5 = ["--queue_limit", "10000"]
        param6 = ["--window_size", str(i)]
        subprocess.call(["python3", "simulator.py"] + param1 + param2 + param3 + param4 + param5 + param6, shell=False)
