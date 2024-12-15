import random
import sys
from collections import defaultdict


class Packet:
    def __init__(self, input_port, output_port, arrival_tick):
        self.input_port = input_port
        self.output_port = output_port
        self.arrival_tick = arrival_tick


# User-supplied parameters
NUM_PORTS = int(sys.argv[1])
ARRIVAL_PROB = float(sys.argv[2])
SEED = int(sys.argv[3])
PIM_ITERS = int(sys.argv[4])  # Number of PIM iterations

# Total number of simulation ticks
NUM_TICKS = 20000

# Seed random number generator
random.seed(SEED)

# variables to compute average delay of packets transmitted out of output ports
delay_count = 0
delay_sum = 0.0

# Virtual output queues at each input
# Initialized to empty queue for each combination of input port and output port
# These queues sit on the input side.
voqs = []
for input_port in range(NUM_PORTS):
    voqs += [[]]
    for output_port in range(NUM_PORTS):
        voqs[input_port] += [[]]

# Main simulator loop: Loop over ticks
for tick in range(NUM_TICKS):
    # Tick every input port
    for input_port in range(NUM_PORTS):
        # Is there a packet here?
        if random.random() < ARRIVAL_PROB:
            # If so, pick output port uniformly at random
            output_port = random.randint(0, NUM_PORTS - 1)
            voqs[input_port][output_port] += [Packet(input_port, output_port, tick)]

    # TODO: Implement PIM algorithm with a single iteration.
    matched_input_ports = set()
    matched_output_port = set()
    for i in range(PIM_ITERS):
        # request phase
        forward_req = defaultdict(list)
        for output_port in range(NUM_PORTS):
            for input_port in range(NUM_PORTS):
                if voqs[input_port][output_port] and input_port not in matched_input_ports \
                        and output_port not in matched_output_port:
                    forward_req[output_port].append(input_port)

        # grant phase
        backup_grant = defaultdict(list)
        for output_port in range(NUM_PORTS):
            if not forward_req[output_port]:
                continue
            grant_queue_idx = random.choice(forward_req[output_port])
            backup_grant[grant_queue_idx].append(output_port)

        # accept phase
        for input_port in range(NUM_PORTS):
            if not backup_grant[input_port]:
                continue
            evict_voq_idx = random.choice(backup_grant[input_port])

            # TODO: Update the average delay every time a packet is dequeued from a VOQ as a result of the matching process.
            # Otherwise, your average delay will be 0/0 because no samples would have been accumulated.
            dequeued_pkt = voqs[input_port][evict_voq_idx].pop(0)
            matched_input_ports.add(input_port)
            matched_output_port.add(evict_voq_idx)
            delay = tick - dequeued_pkt.arrival_tick
            delay_sum += delay
            delay_count += 1

    # TODO: Generalize this to multiple iterations by simply running the same code in a loop a fixed number of times
    # Each iteration must only consider inputs+outputs that are still unmatched after the previous iterations.

    # For both variants of PIM, if input I is matched to output O, complete the matching by dequeueing from voqs[I][O].

    # Average delay printing
    if tick % 100 == 0:
        print("Average delay after ", tick, " ticks = ", delay_sum / delay_count, " ticks")
        # fp = None
        # if PIM_ITERS == 1:
        #     fp = open("pim.txt", "a")
        # elif PIM_ITERS == 2:
        #     fp = open("pim_two.txt", "a")
        # else:
        #     continue
        #
        # if tick == NUM_TICKS - 100:
        #     fp.write(str(delay_sum / delay_count) + "\n")
        # else:
        #     fp.write(str(delay_sum / delay_count) + ",")
        #
        # fp.close()

print()
