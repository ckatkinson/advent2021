def get_input(path):
    with open(path) as f:
        info = [x for x in f][0]
        splitup = info.split(",")
        return [int(x) for x in splitup]


def fuelSpentToPoint(crabs, point):
    """
    Returns the sum of distances from each crab to the point
    """
    return sum([abs(crab - point) for crab in crabs])


def bestMeetingPoint(crabs):
    """
    Computes the fuel-minimizing point
    """
    m, M = min(crabs), max(crabs)
    distances = {fuelSpentToPoint(crabs, i): i for i in range(m, M + 1)}
    closest = min(distances)
    return distances[closest]


def singleCrabFuel(crab, point):
    """ "
    New fuel expediture for part 2
    """
    n = abs(crab - point)
    return n * (n + 1) // 2


def moreFuelSpent(crabs, point):
    """
    Using the singleCrabFuel function to get total spent.
    """
    return sum([singleCrabFuel(crab, point) for crab in crabs])


def bestMeetingPointWithFuel(crabs):
    """
    Using the new fuel calculation to do part 2.
    """

    m, M = min(crabs), max(crabs)
    distances = {moreFuelSpent(crabs, i): i for i in range(m, M + 1)}
    closest = min(distances)
    return distances[closest]


def answer1():
    crabs = get_input("./inputs/seven.txt")
    return fuelSpentToPoint(crabs, bestMeetingPoint(crabs))


def answer2():
    crabs = get_input("./inputs/seven.txt")
    return moreFuelSpent(crabs, bestMeetingPointWithFuel(crabs))


def main():
    print(f"Part 1: {answer1()}")
    print(f"Part 2: {answer2()}")


if __name__ == "__main__":
    main()
