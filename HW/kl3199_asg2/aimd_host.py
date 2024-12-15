import sys
from packet import *
from timeout_calculator import *


class UnackedPacket:
    """
    Structure to store information associated with an unacked packet
    so that we can maintain a list of such UnackedPacket objects

    Data members of this class include

    seq_num:  Sequence number of the unacked packet

    num_retx: Number of times this packet has been retransmitted so far

    timeout_duration: Timeout duration for this packet

    timeout_tick: The time (in ticks) at which the packet timeout

    """

    def __init__(self, seq_num):
        """
        Constructor for UnackedPacket. This sets the default values for class data members

        """
        self.seq_num = seq_num  # sequence number of unacked packet
        self.num_retx = 0  # how many times it's been retransmitted so far
        self.timeout_duration = 0  # what is the duration of its timeout
        self.timeout_tick = 0  # at what tick does this packet timeout?

    def __str__(self):
        """
        String representation of unacked packet for debugging

        """
        return str(self.seq_num)


class AimdHost:
    """
    This class implements a host that follows the AIMD protocol.
    Data members of this class are

    **unacked**: List of unacked packets

    **window**: Size of the window at any given moment

    **max_seq**: Maximum sequence number sent so far

    **in_order_rx_seq**: Maximum sequence number received so far

    **slow_start**: Boolean to indicate whether algorithm is in slow start or not

    **next_decrease**: Time (in ticks) at which the window size should be descreased

    **timeout_calculator**: An object of class TimeoutCalculator
    (Refer to TimeoutCalculator class for more information)

    There are two member functions - send and recv that perform the task of sending
    and receiving packets respectively. All send and receive logic should be written
    within one of these two functions.

    """

    def __init__(self):
        self.unacked = []  # list of unacked packets
        self.window = 1  # We'll initialize window to 1
        self.max_seq = -1  # maximum sequence number sent so far
        self.in_order_rx_seq = -1  # maximum sequence number received so far in order
        self.slow_start = True  # Are we in slow start?
        self.next_decrease = -1  # When to next decrease your window; adds some hystersis
        self.timeout_calculator = TimeoutCalculator()  # object for computing timeouts

    def send(self, tick):
        """
        Function to send packet on to the network. Host should first retransmit any
        Unacked packets that have timed out. Host should also decrease the window size
        if it is time for the next decrease. After attempting retransmissions, if the window
        is not full, fill up the window with new packets.

        Args:

            **tick**: Simulated time

        Returns:

            A list of packets that the host wants to transmit on to the network
        """
        print("@ tick " + str(tick) + " window is " + str(self.window))
        # file1 = open("window.txt", "a")
        # file1.write(str(self.window) + "\n")
        # file1.close()

        # TODO: Create an empty list of packets that the host will send
        to_send = []

        # First, process retransmissions
        for i in range(0, len(self.unacked)):
            unacked_pkt = self.unacked[i]
            if (tick >= unacked_pkt.timeout_tick):
                # TODO: Retransmit any packet that has timed out
                # by doing the following in order
                # (1) creating a new packet,
                packet = Packet(tick, unacked_pkt.seq_num)
                # (2) setting its retx attribute to True (just for debugging)
                packet.retx = True
                # (3) Append the packet to the list of packets created earlier
                to_send.append(packet)
                # (4) Backing off the timer
                self.timeout_calculator.exp_backoff()
                # (5) Updating timeout_tick and timeout_duration appropriately after backing off the timer
                unacked_pkt.timeout_tick = tick + self.timeout_calculator.timeout
                unacked_pkt.timout_duration = self.timeout_calculator.timeout
                # (6) Updating num_retx
                unacked_pkt.num_retx += 1

                # TODO: Multiplicative decrease, if it's time for the next decrease
                # Cut window by half, but don't let it go below 1
                if tick >= self.next_decrease:
                    self.window = self.window / 2 if self.window / 2 >= 1.0 else 1.0

                # TODO: Make sure the next multiplicative decrease doesn't happen until an RTT later
                # (use the timeout_calculator to estimate the RTT)
                if self.next_decrease < tick:
                    self.next_decrease += self.timeout_calculator.mean_rtt

                # Exit slow start, whether you were in it or not
                self.slow_start = False

            self.unacked[i] = unacked_pkt

        # Now fill up the window with new packets
        while len(self.unacked) < self.window:
            # TODO: Create new packets, set their retransmission timeout, and transmit them
            self.max_seq += 1
            packet = Packet(tick, self.max_seq)
            to_send.append(packet)
            # TODO: Remember to update self.max_seq and add the just sent packet to self.unacked
            unacked_pkt = UnackedPacket(self.max_seq)
            unacked_pkt.timeout_tick = tick + self.timeout_calculator.timeout
            unacked_pkt.timeout_duration = self.timeout_calculator.timeout
            self.unacked.append(unacked_pkt)

        # TODO: Return the list of packets that need to be sent on to the network
        return to_send

    def recv(self, pkt, tick):
        """
        Function to get a packet from the network.

        Args:

            **pkt**: Packet received from the network

            **tick**: Simulated time
        """
        assert (tick > pkt.sent_ts)
        # TODO: Compute RTT sample
        rtt_sample = tick - pkt.sent_ts
        # TODO: Update timeout
        self.timeout_calculator.update_timeout(rtt_sample)
        # TODO: Remove received packet from self.unacked
        filtered_unacked = [unacked_pkt for unacked_pkt in self.unacked if unacked_pkt.seq_num != pkt.seq_num]
        self.unacked = filtered_unacked
        # TODO: Update in_order_rx_seq to reflect the largest sequence number that you
        # have received in order so far
        self.in_order_rx_seq = max(self.in_order_rx_seq, pkt.seq_num)
        # TODO: Increase your window given that you just received an ACK. Remember that:
        # 1. The window increase rule is different for slow start and congestion avoidance.
        # 2. The recv() function is called on every ACK (not every RTT), so you should adjust your window accordingly.
        self.window += (1 if self.slow_start else 1 / self.window)
