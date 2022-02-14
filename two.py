
def read_file(file):
    with open(file) as f:
        return [tuple(line.split()) for line in f]

class Sub():
    def __init__(self):
        self.pos = 0
        self.depth = 0
    def move(self, op):
        direction = op[0]
        distance = int(op[1])
        if direction == "forward":
            self.pos += distance
        elif direction == "down":
            self.depth += distance
        else:
            self.depth -= distance

class SubAim():
    def __init__(self):
        self.pos = 0
        self.depth = 0
        self.aim = 0
    def move(self, op):
        direction = op[0]
        amt = int(op[1])
        if direction == "forward":
            self.pos += amt
            self.depth += self.aim * amt
        elif direction == "down":
            self.aim += amt
        else:
            self.aim -= amt



def main():
    S, T = Sub(), SubAim()
    ops = read_file('./inputs/two.txt')
    for op in ops:
        S.move(op)
        T.move(op)
    print(f"Part 1: {S.pos * S.depth}")
    print(f"Part 2: {T.pos * T.depth}")

if __name__ == "__main__":
    main()
