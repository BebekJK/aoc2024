def split_line(line):
    line = line.split(':')
    res = int(line[0])
    op = line[1].strip().split(' ')
    op = [int(o) for o in op]
    return res, op

# Part One
def solve_part_one():
    def is_valid(res, op, curr, index):
        if index == len(op):
            return res == curr
        return is_valid(res, op, curr + op[index], index + 1) or is_valid(res, op, curr * op[index], index + 1)
    
    with open('input/day7.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        ans = sum([res if is_valid(res, op, op[0], 1) else 0 for res, op in data])
        
        print(f"Answer for part one: {ans}")
# Part Two
def solve_part_two():
    def is_valid(res, op, curr, index):
        if index == len(op):
            return res == curr
        return is_valid(res, op, curr + op[index], index + 1) or is_valid(res, op, curr * op[index], index + 1) or is_valid(res, op, int(str(curr)+str(op[index])), index + 1)
    
    with open('input/day7.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        ans = sum([res if is_valid(res, op, op[0], 1) else 0 for res, op in data])
        
        print(f"Answer for part one: {ans}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()