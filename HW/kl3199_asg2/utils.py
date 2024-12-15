import matplotlib.pyplot as plt
import numpy as np


def plot_congestion_collapse():
    file1 = open('congestion_collapse.txt', 'r')
    lines = file1.readlines()
    throughputs = [int(line.strip()) / 100000 for line in lines]
    window_sizes = [i for i in range(1, 1000, 10)] + [1000]
    plt.plot(window_sizes, throughputs)
    plt.xlabel("Window Size")
    plt.ylabel("Throughput")
    plt.show()


# ticks = 10000   window size = 5  variable: rtt_min
# 5  0.9996
# 6  0.8240
# 7  0.7140
# 8  0.6246
# 9  0.5552
# 10 0.4996
def plot_swp_result1():
    x = [i for i in range(5, 11)]
    y = [0.9996, 0.824, 0.714, 0.6246, 0.5552, 0.4996]
    predicted = [5 / i for i in range(5, 11)]
    plt.plot(x, y)
    plt.plot(x, predicted)
    plt.xlabel("RTT_min")
    plt.ylabel("Throughput")
    plt.legend(["actual", "predicted"])
    plt.show()


# ticks = 10000    rtt_min = 10   variable: window size
# 0.1, 0.1999, 0.2998, 0.3996, 0.4996, 0.5995, 0.6994, 0.7993, 0.8992, 0.9991
def plot_swp_result2():
    x = [i for i in range(1, 11)]
    y = [0.1, 0.1999, 0.2998, 0.3996, 0.4996, 0.5995, 0.6994, 0.7993, 0.8992, 0.9991]
    predicted = [i / 10 for i in range(1, 11)]
    plt.plot(x, y)
    plt.plot(x, predicted)
    plt.xlabel("Window size")
    plt.ylabel("Throughput")
    plt.legend(["actual", "predicted"])
    plt.show()


# ticks = 10000  rtt_min = 10   loss_ratio = 0.01   variable: window size
# 0.4556, 0.5421, 0.6338, 0.7223, 0.8902, 0.8989
def plot_swp_result3():
    x = [i for i in range(5, 11)]
    y = [0.4556, 0.5421, 0.6338, 0.7223, 0.8902, 0.8989]
    predicted = [i / 10 for i in range(5, 11)]
    plt.plot(x, y)
    plt.plot(x, predicted)
    plt.xlabel("Window size")
    plt.ylabel("Throughput")
    plt.legend(["actual", "predicted"])
    plt.show()


# ticks = 10000  window_size = 5   loss_ratio = 0.01   rtt_min
# 0.8168, 0.6982, 0.6202, 0.5512, 0.4948, 0.4556
def plot_swp_result4():
    x = [i for i in range(5, 11)]
    y = [0.8168, 0.6982, 0.6202, 0.5512, 0.4948, 0.4556]
    predicted = [5 / i for i in range(5, 11)]
    plt.plot(x, y)
    plt.plot(x, predicted)
    plt.xlabel("RTT_min")
    plt.ylabel("Throughput")
    plt.legend(["actual", "predicted"])
    plt.show()


def plot_aimd_result():
    file1 = open('window.txt', 'r')
    lines = file1.readlines()
    throughputs = [float(line.strip()) for line in lines]
    window_sizes = [i for i in range(1, len(throughputs) + 1)]
    plt.plot(window_sizes, throughputs)
    my_x_ticks = np.arange(0, 10001, 1000)
    plt.xticks(my_x_ticks)
    plt.xlabel("Time in ticks")
    plt.ylabel("Window size in packets")
    plt.show()


if __name__ == '__main__':
    # plot_congestion_collapse()
    # plot_swp_result1()
    # plot_swp_result2()
    # plot_swp_result3()
    plot_swp_result4()
    # plot_aimd_result()
