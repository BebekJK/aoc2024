def split_line(line):
    line = line.split(' ')
    return int(line[0]), int(line[-1])

# Part One
def solve_part_one():
    with open('input/day4.txt') as f:
        grid = f.read().splitlines()
        dx = [1, 1, 0, -1, -1, -1, 0, 1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]
        
        ans = 0
        
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                for k in range(8):
                    if i + 3*dx[k] >= 0 and i + 3*dx[k] < len(grid) and j + 3*dy[k] >= 0 and j + 3*dy[k] < len(row):
                        if grid[i][j] == 'X' and grid[i + dx[k]][j + dy[k]] == 'M' and grid[i + 2*dx[k]][j + 2*dy[k]] == 'A' and grid[i + 3*dx[k]][j + 3*dy[k]] == 'S':
                            ans += 1
        
        print(f"Answer for part one: {ans}")

# Part Two
def solve_part_two():
    def check_xmas(arr):
        if arr[1][1] != 'A':
            return 0
        
        if arr[0][0] == 'M' and arr[2][2] == 'S' and arr[0][2] == 'M' and arr[2][0] == 'S':
            return 1
        if arr[0][0] == 'M' and arr[2][2] == 'S' and arr[0][2] == 'S' and arr[2][0] == 'M':
            return 1
        if arr[0][0] == 'S' and arr[2][2] == 'M' and arr[0][2] == 'M' and arr[2][0] == 'S':
            return 1
        if arr[0][0] == 'S' and arr[2][2] == 'M' and arr[0][2] == 'S' and arr[2][0] == 'M':
            return 1
        
        return 0
    with open('input/day4.txt') as f:
        grid = f.read().splitlines()
        ans = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if i + 2 < len(grid) and j + 2 < len(row):
                    ans += check_xmas([list(row[j:j+3]) for row in grid[i:i+3]])
        
        print(f"Answer for part two: {ans}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()