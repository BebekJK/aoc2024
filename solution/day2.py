def split_line(line):
    line = line.split(' ')
    line = [int(i) for i in line]
    return line

def is_increasing_safe(arr):
    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1] or arr[i] - arr[i+1] > 3:
            return False
    return True

def is_decreasing_safe(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1] or arr[i+1] - arr[i] > 3:
            return False
    return True

def is_safe(arr):
    return is_increasing_safe(arr) or is_decreasing_safe(arr)

# Part One
def solve_part_one():
    with open('input/day2.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        safe = [is_safe(line) for line in data]
        count = sum(safe)
        
        print(f"Answer for part one: {count}")
        
# Part Two
def solve_part_two():
    with open('input/day2.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        safe = [False for line in data]
        for arr in data:
            for i in range(len(arr)):
                if is_safe(arr[:i] + arr[i+1:]):
                    safe[data.index(arr)] = True
                    break
        count = sum(safe)
        
        print(f"Answer for part two: {count}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()