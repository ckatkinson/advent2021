"""
  0:6     1:2     2:5     3:5     4:4
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:5     6:6     7:3     8:7    9:6
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

A logic puzzle! I see the prompt for part 1 doesn't
require full decoding, but I'm going to do it anyways.

"""

import re


def get_input(file):
    with open(file) as f:
        raw = [[str(x) for x in re.split(" | \| |\|", line[:-1])] for line in f]
        return [(x[:10], x[-4:]) for x in raw]


segmentsToDigitDict = {
    "abcefg": 0,  # 6
    "cf": 1,  # 2
    "acdeg": 2,  # 5
    "acdfg": 3,  # 5
    "bcdf": 4,  # 4
    "abdfg": 5,  # 5
    "abdefg": 6,  # 6
    "acf": 7,  # 3
    "abcdefg": 8,  # 7
    "abcdfg": 9,  # 6
}


def lengthToStringDict(strings):
    output = {}
    for s in strings:
        if len(s) in output:
            output[len(s)].append(set(s))
        else:
            output[len(s)] = [set(s)]
    return output


def identifySegments(jumble):
    """

    Here's my procedure for finding the letters.

    a = symm diff of length-2 and length-3 (from 1 and 7)
    f = intersection of length-2 with length 6 such that there is only one symbol
    bd = symm diff of length-2 and length-4 (from 1 and 4)
    abfg = intersection of all three length-6 (0, 6, 9)
    g = symm diff of abg and (a U bd)
    b = symm diff of abg and (a U g)
    d = symm dif of b with bd
    c = symm diff of length-2 with f
    e = symm diff of a U b U c U d U f U g

    """

    lengthDict = lengthToStringDict(jumble)
    output = {}

    # Follow the above scheme to find everything. These are set ops. Once we have singletons, we'll
    # pop them all into a dict.

    a = lengthDict[3][0] - lengthDict[2][0]
    bd = lengthDict[4][0] - lengthDict[2][0]
    f = [
        lengthDict[2][0] & six
        for six in lengthDict[6]
        if len(lengthDict[2][0] & six) == 1
    ][0]
    abfg = lengthDict[6][0] & lengthDict[6][1] & lengthDict[6][2]
    g = abfg - (a | bd | f)
    b = abfg - (a | g | f)
    d = bd - b

    c = lengthDict[2][0] - f
    e = lengthDict[7][0] - (a | b | c | d | f | g)

    output[a.pop()] = "a"
    output[b.pop()] = "b"
    output[c.pop()] = "c"
    output[d.pop()] = "d"
    output[e.pop()] = "e"
    output[f.pop()] = "f"
    output[g.pop()] = "g"

    return output


def decodeNumber(decoder, code):
    """
    decoder should be a dict that takes [a-f] to [a-f]
    """
    decoded = "".join(sorted([decoder[x] for x in code]))
    return segmentsToDigitDict[decoded]


def decodeAllLines(input):
    """
    Run the decoder on every line of the input file, formatted as output from the get_input function.
    """
    output = []
    for line in input:
        testDigits = line[0]
        message = line[1]
        decoder = identifySegments(testDigits)
        output.append([decodeNumber(decoder, x) for x in message])
    return output


def answer1():
    inputfile = get_input("./inputs/eight.txt")
    decoded = decodeAllLines(inputfile)
    cond = lambda x: x == 1 or x == 4 or x == 7 or x == 8

    return len([entry for line in decoded for entry in line if cond(entry)])


def convertToDecimal(digs):
    """
    convert length-4 list to decimal for computing answer 2.
    """
    return sum([(10**i) * x for i, x in zip(range(3, -1, -1), digs)])


def answer2():
    inputfile = get_input("./inputs/eight.txt")
    decoded = decodeAllLines(inputfile)
    return sum([convertToDecimal(x) for x in decoded])


def main():
    print(f"Part 1: {answer1()}")
    print(f"Part 2: {answer2()}")


if __name__ == "__main__":
    main()
