from dis import findlabels
from pickletools import uint2
import numpy as np


def read_file(file):
    with open(file) as f:
        return np.array([np.array([int(x) for x in line[:-1]]) for line in f])


testfile = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]
test = np.array([np.array([int(x) for x in line]) for line in testfile])


def gamma(report):
    return np.round(sum(report) / len(report)).astype(int)


def epsilon(report):
    return np.logical_not(gamma(report)).astype(int)


def fiveBitToInt(arr):
    return arr.dot(2 ** np.arange(len(arr) - 1, -1, -1))


def oxygen(lines):
    for i in range(len(lines[0])):
        gam = gamma(lines)

        if len(lines) == 1:
            return fiveBitToInt(lines[0])
        elif len(lines[[line[i] == 1 for line in lines]]) == len(
            lines[[line[i] == 0 for line in lines]]
        ):
            lines = lines[[line[i] == 1 for line in lines]]
        else:
            lines = lines[[line[i] == gam[i] for line in lines]]
    return fiveBitToInt(lines[0])


def carbondioxide(lines):

    for i in range(len(lines[0])):
        eps = epsilon(lines)
        if len(lines) == 1:
            return fiveBitToInt(lines[0])
        elif len(lines[[line[i] == 1 for line in lines]]) == len(
            lines[[line[i] == 0 for line in lines]]
        ):
            lines = lines[[line[i] == 0 for line in lines]]
        else:
            lines = lines[[line[i] == eps[i] for line in lines]]
    return fiveBitToInt(lines[0])


def main():
    lines = read_file("./inputs/three.txt")
    print(f"Part 1: {fiveBitToInt(gamma(lines)) * fiveBitToInt(epsilon(lines))}")
    print(f"Part 2: {oxygen(lines) * carbondioxide(lines)}")


if __name__ == "__main__":
    main()
