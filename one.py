def read_file_to_list(file):
    with open(file,'r') as f:
        return [int(line) for line in f]

def num_increases(lines):
    return sum([1 for i in range(1,len(lines)) if lines[i] > lines[i-1]])

line_iter = read_file_to_list("./inputs/one.txt")
print(f"Part 1: {num_increases(line_iter)}")

def sum3(lines):
    return [lines[i-2] + lines[i-1] + lines[i] for i in range(2, len(lines))]

print(f"Part 2: {num_increases(sum3(line_iter))}")