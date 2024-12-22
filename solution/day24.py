def split_line(line):
    line = line.split(' ')
    line = [int(i) for i in line]
    return line

# Part One
def solve_part_one():
    with open('input/day24.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        
        # print(f"Answer for part one: {ans}")
        
# Part Two
def solve_part_two():
    with open('input/day24.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        
        # print(f"Answer for part two: {ans}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()