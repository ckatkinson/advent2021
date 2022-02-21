import numpy as np


def get_input(file):
    with open(file) as f:
        return np.array([list(line[:-1]) for line in f], dtype=int)


def neighbors(pos, array):
    """
    This is a slog. While typing it, I started realizing fragments of better ways, but I'm not sure if it's worth worrying about. I'm assuming the array is square, as it is in the problem.
    """
    x, y = pos
    xdim, _ = array.shape
    bottomQ = lambda z: z == 0
    topQ = lambda z: z == xdim - 1
    edgeQ = lambda z: bottomQ(z) and topQ(z)

    if bottomQ(x) and bottomQ(y):
        return [(x + 1, y), (x, y + 1)]
    elif bottomQ(x) and topQ(y):
        return [(x + 1, y), (x, y - 1)]
    elif topQ(x) and bottomQ(y):
        return [(x - 1, y), (x, y + 1)]
    elif topQ(x) and topQ(y):
        return [(x - 1, y), (x, y - 1)]
    elif bottomQ(x):
        return [(x, y - 1), (x, y + 1), (x + 1, y)]
    elif bottomQ(y):
        return [(x - 1, y), (x + 1, y), (x, y + 1)]
    elif topQ(x):
        return [(x, y - 1), (x, y + 1), (x - 1, y)]
    elif topQ(y):
        return [(x - 1, y), (x + 1, y), (x, y - 1)]
    else:
        return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def isMinimumQ(pos, grid):
    """
    Is postion a local min?
    """
    nbrs = neighbors(pos, grid)
    return np.all([grid[pos] < grid[n] for n in nbrs])


def allLocalMinValues(grid):
    """
    Return value of all local minimumns in the array
    """
    xdim, _ = grid.shape
    return np.array(
        [
            grid[(x, y)]
            for x in range(xdim)
            for y in range(xdim)
            if isMinimumQ((x, y), grid)
        ]
    )


def answer1():
    grid = get_input("./inputs/nine.txt")
    minvals = allLocalMinValues(grid)
    risk = minvals + 1
    return sum(risk)


def allLocalMinPositions(grid):
    """
    Return location of all local minimumns in the array. Could rewrite the value one above to use this.
    """
    xdim, _ = grid.shape
    return np.array(
        [(x, y) for x in range(xdim) for y in range(xdim) if isMinimumQ((x, y), grid)]
    )


def neighborsInBasin(pos, grid):
    """
    Find the neighbors of pos in the basis containing pos. If the value at a neighbor is 9, it
    isn't included because that's on the boundary of the basin.
    """
    return set([neigh for neigh in neighbors(pos, grid) if grid[neigh] != 9])


"""
Here's the plan:
1) mins = nparray of minimum locations
2) For each position in grid that's not yet tagged with a basin, if it's not 9, make an expanding set of neighborsInBasin until a min is in the neighborhood. Tag EVERY location in that set with the min location.

I think this is basically some sort of dijkstra's algorithm type thing.
"""

# TODO: Speed this thing up. Can do by keeping track of the frontier of the expanding neighborhood.
# We're repeating a lot of work by always looking at neighbors of interior points.
def traverseBasinToMin(pos, grid):
    """
    Produce set of locations seen while looking for the min in the basin containing pos. Returns (setOfLocs, minLoc)
    """
    pos = tuple(pos)
    mins = set([tuple(place) for place in allLocalMinPositions(grid)])
    seen = set([pos])
    frontier = seen
    if pos in mins:
        return (seen, pos)
    while len(mins & seen) == 0:
        for loc in seen:
            seen = seen | neighborsInBasin(loc, grid)
    minLoc = (mins & seen).pop()
    return (seen, minLoc)


# Seems to work, but is (predictably) very slow. See comment above transverseBasin function
# for a way to speed this up.
def dictOfBasinMin(grid):
    """
    For every position, traverse to min and tag every point seen with its min.
    """
    xdim, _ = grid.shape
    allPositions = [(x, y) for x in range(xdim) for y in range(xdim)]
    output = {}
    print("This takes like 30s. Be patient.")
    for pos in allPositions:
        if grid[pos] == 9:
            continue
        if not pos in output:
            seen, minLoc = traverseBasinToMin(pos, grid)
            for place in seen:
                output[place] = minLoc
    return output


def answer2():
    grid = get_input("./inputs/nine.txt")
    d = dictOfBasinMin(grid)
    basins = {minv: [pos for pos in d.keys() if d[pos] == minv] for minv in d.values()}
    basinls = [len(v) for v in basins.values()]
    basinls.sort(reverse=True)
    return basinls[0] * basinls[1] * basinls[2]


def main():
    print(f"Part 1: {answer1()}")
    print(f"Part 2: {answer2()}")


if __name__ == "__main__":
    main()
