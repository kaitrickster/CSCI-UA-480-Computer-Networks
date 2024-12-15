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

# Total number of simulation ticks
NUM_TICKS = 20000

# Seed random number generator
random.seed(SEED)

# variables to compute average delay of packets transmitted out of output ports
delay_count = 0
delay_sum = 0.0

# One input queue for each input port
# Initialized to empty queue for each input port
input_queues = []
for input_port in range(NUM_PORTS):
    input_queues += [[]]

# Main simulator loop: Loop over ticks
for tick in range(NUM_TICKS):
    # Tick every input port
    for input_port in range(NUM_PORTS):
        # Is there a packet here?
        if random.random() < ARRIVAL_PROB:
            # If so, pick output port uniformly at random
            output_port = random.randint(0, NUM_PORTS - 1)
            input_queues[input_port] += [Packet(input_port, output_port, tick)]

    # TODO: Implement FIFO algorithm:
    # First, look at all the head packets, i.e., packets at the head of each of the input_queues
    # Second, If multiple inputs have head packets destined to the same output port,
    # pick an input port at random, and deq from that. Repeat for each output port.
    d = defaultdict(list)
    for o in range(NUM_PORTS):
        for input_port in range(NUM_PORTS):
            input_queue = input_queues[input_port]
            if input_queue and input_queue[0].output_port == o:
                d[o].append(input_port)

    # More detailed instructions for FIFO algorithm:
    # First, populate a dictionary d that maps an output port to the list of all packets destined to that output.
    # Second, for each output port o, pick one of the packets in the list d[o] at random
    # To pick one packet out of a list at random, you can use the random.choice function.
    # Note: To complete the matching for an input port i that was picked and hence matched to an output port,
    # dequeue from that input port's queue (input_queues[i])

    # TODO: Update the average delay based on the packets that were just dequeued.
    # Otherwise, your average delay will be 0/0 because no samples would have been accumulated.
    for o in range(NUM_PORTS):
        if not d[o]:
            continue
        evict_input_port = random.choice(d[o])
        dequeued_pkt = input_queues[evict_input_port].pop(0)
        delay = tick - dequeued_pkt.arrival_tick
        delay_sum += delay
        delay_count += 1

    # Average delay printing
    if tick % 100 == 0:
        print("Average delay after ", tick, " ticks = ", delay_sum / delay_count, " ticks")
        # fp = open("fifo.txt", "a")
        #
        # if tick == NUM_TICKS - 100:
        #     fp.write(str(delay_sum / delay_count) + "\n")
        # else:
        #     fp.write(str(delay_sum / delay_count) + ",")
        #
        # fp.close()
print()
