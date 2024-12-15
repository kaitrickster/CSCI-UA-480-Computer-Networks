import sys
from packet import *
from timeout_calculator import *


class UnackedPacket:
    """
    Structure to store information associated with an unacked packet
    so that we can maintain a list of such UnackedPacket objects.

    This structure is different from the packet structure that is used
    by the simulator. Be careful to not mix Packet and UnackedPacket

    The network does not understand an UnackedPacket. It is only used by
    sliding window host for bookkeeping.
    """

    def __init__(self, seq_num):
        self.seq_num = seq_num  # sequence number of unacked packet
        self.num_retx = 0  # how many times it's been retransmitted so far
        self.timeout_duration = 0  # what is the duration of its timeout
        self.timeout_tick = 0  # at what tick does this packet timeout?

    def __str__(self):  # string representation of unacked packet for debugging
        return str(self.seq_num)


class SlidingWindowHost:
    """
    This host follows the SlidingWindow protocol. It maintains a window size and the
    list of unacked packets. The algorithm itself is documented with the send method
    """

    def __init__(self, window_size):
        self.unacked = []  # list of unacked packets
        self.window = window_size  # window size
        self.max_seq = -1  # maximum sequence number sent so far
        self.in_order_rx_seq = -1  # maximum sequence number received so far in order
        self.timeout_calculator = TimeoutCalculator()  # object for computing timeouts
        self.retransmitted = set()  # used to analyze congestion collapse

    def send(self, tick):
        """
        Method to send packets on to the network. Host must first check if there are any
        unacked packets, it yes, it should retransmist those first. If the window is still
        empty, the host can send more new packets on to the network.

        Args:

            **tick**: Current simulated time

        Returns:
            A list of packets that need to be transmitted. Even in case of a single packet,
            it should be returned as part of a list (i.e. [packet])
        """
        # TODO: Create an empty list of packets that the host will send
        to_send = []

        # First, process retransmissions
        for i in range(0, len(self.unacked)):
            unacked_pkt = self.unacked[i]
            if tick >= unacked_pkt.timeout_tick:
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

                # catch point: used to analyze congestion collapse
                # self.retransmitted.add(unacked_pkt.seq_num)
                # print(f"------ {len(self.retransmitted)} packets retransmitted ------")
                # print(f"----- retransmission detected @ tick {tick} with seq num {unacked_pkt.seq_num}-----")

            self.unacked[i] = unacked_pkt

        assert (len(self.unacked) <= self.window)

        # Now fill up the window with new packets
        while len(self.unacked) < self.window:
            # TODO: Create new packets, set their retransmission timeout, and add them to the list
            # TODO: Remember to update self.max_seq and add the just sent packet to self.unacked
            self.max_seq += 1
            packet = Packet(tick, self.max_seq)
            to_send.append(packet)

            # debug
            print(f"sent packet @ {tick} with sequence number {self.max_seq}")
            # print(f"packet {self.max_seq} 's timeout tick is {packet}")

            unacked_pkt = UnackedPacket(self.max_seq)
            unacked_pkt.timeout_tick = tick + self.timeout_calculator.timeout
            unacked_pkt.timeout_duration = self.timeout_calculator.timeout
            self.unacked.append(unacked_pkt)

            # print(f"packet {self.max_seq} 's timeout tick is {unacked_pkt.timeout_tick}")

        # window must be filled up at this point
        assert (len(self.unacked) == self.window)

        # TODO: return the list of packets that need to be transmitted on to
        # the network
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

        assert (len(self.unacked) <= self.window)
