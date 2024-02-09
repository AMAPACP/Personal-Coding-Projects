import numpy as np
from matplotlib import pyplot as plt


def print_hi():
    flips = int(input("How many coin flips in total?: "))
    trials = int(input("How many trials: "))
    maxi_result = list()
    for i in range(trials):
        maxi = 0
        index = 0
        flips_list = np.random.random(flips) > 0.5
        while not index == len(flips_list):
            current = 0
            if not flips_list[index]:
                index += 1
                continue
            while not index == len(flips_list):
                if not flips_list[index]:
                    break
                index += 1
                current += 1
            if maxi < current:
                maxi = current
        maxi_result.append(maxi)
    print(np.mean(maxi_result))
    fig, axes = plt.subplots()
    axes.hist(maxi_result, len(set(maxi_result)))
    plt.show()


if __name__ == '__main__':
    print_hi()
