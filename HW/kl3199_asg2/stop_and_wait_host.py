from packet import *
from timeout_calculator import *  # Import timeout calculator for StopAndWait


class StopAndWaitHost:
    """
    This host implements the stop and wait protocol. Here the host only
    sends one packet in return of an acknowledgement.
    """

    def __init__(self):
        self.in_order_rx_seq = -1  # maximum sequence number received so far in order
        self.ready_to_send = True  # can we send a packet or are we still waiting for an ACK?
        self.packet_sent_time = -1  # when was this packet sent out last?
        self.timeout_calculator = TimeoutCalculator()  # initialize TimeoutCalculator

    def send(self, tick):
        """
        Function to send a packet with the next sequence number on to the network.
        """
        if self.ready_to_send:
            # TODO: Send next sequence number by creating a packet
            pkt = Packet(tick, self.in_order_rx_seq + 1)
            # TODO: Remember to update packet_sent_time and ready_to_send appropriately
            self.packet_sent_time = tick
            self.ready_to_send = False

            # debug
            print(f"sent packet @ {tick} with sequence number {pkt.seq_num}")

            # TODO: Return the packet
            return pkt

        elif tick - self.packet_sent_time >= self.timeout_calculator.timeout:
            # TODO: Timeout has been exceeded, retransmit packet
            # following the same procedure as above when transmitting a packet for the first time
            pkt = Packet(tick, self.in_order_rx_seq + 1)
            self.packet_sent_time = tick
            self.ready_to_send = False

            # debug
            print(f"sent packet @ {tick} with sequence number {pkt.seq_num}")
            print("--------------- retransmission detected ---------------")

            # TODO: Exponentially back off the timer
            self.timeout_calculator.exp_backoff()
            # TODO: Set retx field on packet to detect retransmissions for debugging
            pkt.retx = True
            # TODO: Return the packet
            return pkt

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
        # TODO: Update timeout based on RTT sample
        self.timeout_calculator.update_timeout(rtt_sample)

        # debug
        print(f"@ {tick} timeout computed to be {self.timeout_calculator.timeout}")
        print(f"rx packet @ {tick} with sequence number {pkt.seq_num} \n")

        # TODO: Update self.in_order_rx_seq and self.ready_to_send depending on pkt.seq_num
        if pkt.seq_num == self.in_order_rx_seq + 1:
            self.in_order_rx_seq += 1
            self.ready_to_send = True
