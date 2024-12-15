import numpy as np
import subprocess

probabilities = np.linspace(0.1, 0.9, 9)
algorithms = ["fifo", "pim"]
iterations = [1, 2]
NUM_PORTS = 50

for p in probabilities:
    for algo in algorithms:
        args = None
        if algo == "pim":
            for iteration in iterations:
                args = "python3 pim.py " + str(NUM_PORTS) + " " + str(p) + " 1 " + str(iteration)
                subprocess.call(args, shell=True)

        else:
            args = "python3 fifo.py " + str(NUM_PORTS) + " " + str(p) + " 1"
            subprocess.call(args, shell=True)
