import re
import numpy as np


def get_input(file):
    with open(file) as f:
        return [[int(x) for x in re.split(",|->", line)] for line in f]


def getHorizVert(input):
    """
    Returns vents that are horizontal or vertical
    """
    return [x for x in input if (x[0] == x[2]) or (x[1] == x[3])]


hvs = getHorizVert(get_input("./5test.txt"))


def getBound(vents):
    """
    Returns largest coordinate for building the array.
    """
    M = max([max(x) for x in vents])
    return M


def recordHVvent(vent, array):
    """
    Add vent info to array
    """
    y1, x1, y2, x2 = tuple(vent)
    if x1 == x2:  # vert
        x1, x2 = min([x1, x2]), max([x1, x2])
        y1, y2 = min([y1, y2]), max([y1, y2])
        array[x1, y1 : y2 + 1] += 1
        return array
    elif y1 == y2:  # horiz
        x1, x2 = min([x1, x2]), max([x1, x2])
        y1, y2 = min([y1, y2]), max([y1, y2])
        array[x1 : x2 + 1, y1] += 1
        return array
    elif (y2 - y1) / (x2 - x1) == 1:  # slope is 1
        x1, x2 = min([x1, x2]), max([x1, x2])
        y1, y2 = min([y1, y2]), max([y1, y2])
        for i in range(x2 - x1 + 1):
            array[(x1 + i, y1 + i)] += 1
        return array
    else:  # slope is -1
        x1, x2 = min([x1, x2]), max([x1, x2])
        y1, y2 = max([y1, y2]), min([y1, y2])
        for i in range(x2 - x1 + 1):
            array[(x1 + i, y1 - i)] += 1
        return array


def mapVents(vents):
    """
    Give a list of all HV vents
    """
    M = getBound(vents)
    region = np.zeros((M + 1, M + 1), dtype=int)
    [recordHVvent(vent, region) for vent in vents]
    return region


def answer1(inputFile):
    """Number of locations in HV vents where there are more than one"""
    hvs = getHorizVert(get_input(inputFile))
    ventmap = mapVents(hvs)
    return sum([sum([1 for x in row if x > 1]) for row in ventmap])


def answer2(inputFile):
    """Number of locations in all vents where there are nore than one"""
    vents = get_input(inputFile)
    ventmap = mapVents(vents)
    return sum([sum([1 for x in row if x > 1]) for row in ventmap])


def main():
    print(f"Part 1: {answer1('./inputs/five.txt')}")
    print(f"Part2: {answer2('./inputs/five.txt')}")


if __name__ == "__main__":
    main()
