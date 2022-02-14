from posixpath import split
from xmlrpc.server import SimpleXMLRPCDispatcher

import numpy as np


def get_input(path):
    with open(path) as f:
        info = [x for x in f][0]
        splitup = info.split(",")
        return np.array([int(x) for x in splitup])


def stepFishies(fishies):
    """
    Follow lanternfish proceedure once.
    """
    fishies -= 1
    numBabies = len(fishies[fishies == -1])
    fishies[fishies == -1] = 6  # reset timers on existing fish
    babies = np.full(numBabies, 8)  # new babies
    return np.concatenate((fishies, babies))


def makeSteps(fishies, n):
    """
    Do the fish thing n times.
    """
    for i in range(n):
        fishies = stepFishies(fishies)
    return fishies

def answer1():
    fishies = get_input("./inputs/six.txt")
    return len(makeSteps(fishies, 80))

"""
For part 2, we need to see what happens after 256 steps. The above solution doesn't scale as the length grows exponentially. There's no reason to pay attention to the individual fish, though. Just hold the state with an array where the ith position indicates how many fish have i days on their timer. Tested to be ~20 times faster for the first part.
"""

def collect_fish_times(fishies):
    return np.array([len(fishies[fishies == i]) for i in range(9)])

def stepTimes( fishTimes ):
    zeros = fishTimes[0]
    output = fishTimes[1:]
    output[6] += zeros
    return np.append(output, zeros)

def takeTimeSteps( fishTimes, n):
    for i in range(n):
        fishTimes = stepTimes(fishTimes)
    return fishTimes

def answer2():
    fishies = collect_fish_times(get_input("./inputs/six.txt"))
    return sum(takeTimeSteps(fishies, 256))


def main():
    print(f"Part 1: {answer1()}")
    print(f"Part2: {answer2()}")


if __name__ == "__main__":
    main()

test = np.array([3, 4, 3, 1, 2])
fishies = get_input('./inputs/six.txt')