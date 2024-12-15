import matplotlib.pyplot as plt
import numpy as np


def calculate_fifo_avg_delay():
    file1 = open('fifo.txt', 'r')
    lines = file1.readlines()
    histories = [[float(num_str) for num_str in line.split(",")] for line in lines]
    avg_delays = []
    for i in range(len(histories)):
        avg_delays.append(sum(histories[i]) / len(histories[i]))

    return avg_delays


def calculate_pim_avg_delay():
    file1 = open('pim.txt', 'r')
    lines = file1.readlines()
    histories = [[float(num_str) for num_str in line.split(",")] for line in lines]
    avg_delays = []
    for i in range(len(histories)):
        avg_delays.append(sum(histories[i]) / len(histories[i]))

    return avg_delays


def calculate_pim_two_avg_delay():
    file1 = open('pim_two.txt', 'r')
    lines = file1.readlines()
    histories = [[float(num_str) for num_str in line.split(",")] for line in lines]
    avg_delays = []
    for i in range(len(histories)):
        print(f"sanity check: {len(histories[i])}")
        avg_delays.append(sum(histories[i]) / len(histories[i]))

    return avg_delays


def plot_graph():
    fifo_avg_delay = calculate_fifo_avg_delay()
    pim_avg_delay = calculate_pim_avg_delay()
    pim_two_avg_delay = calculate_pim_two_avg_delay()

    x = np.linspace(0.1, 0.9, 9)
    plt.plot(x, fifo_avg_delay)
    plt.plot(x, pim_avg_delay)
    plt.plot(x, pim_two_avg_delay)
    plt.xlabel("p")
    plt.ylabel("avg delay")
    plt.legend(["FIFO", "PIM", "PIM (2 iterations)"])
    plt.show()


if __name__ == '__main__':
    plot_graph()