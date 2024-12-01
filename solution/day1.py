def split_line(line):
    line = line.split(' ')
    return int(line[0]), int(line[-1])

# Part One
def solve_part_one():
    with open('input/day1.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        left = [line[0] for line in data]
        right = [line[1] for line in data]
        
        left.sort()
        right.sort()
        dist = 0
        
        for l, r in zip(left, right):
            dist += abs(r - l)
        
        print(f"Answer for part one: {dist}")

# Part Two
def solve_part_two():
    with open('input/day1.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        left = [line[0] for line in data]
        right = [line[1] for line in data]
        
        counter = {}
        for i in right:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        similarity = 0
        for i in left:
            if i in counter:
                similarity += counter[i] * i
        
        print(f"Answer for part two: {similarity}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()