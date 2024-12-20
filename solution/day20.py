memo = None
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def next_dir(dir):
    return (dir + 1) % 4

def prev_dir(dir):
    return (dir + 3) % 4

def reset(r, c):
    global memo
    memo = [[10**6 for _ in range(c)] for _ in range(r)]

def iterate(grid, start, end):
    reset(len(grid), len(grid[0]))
    queue = []
    queue.append((start, 0))
    memo[start[0]][start[1]] = 0
    
    while queue:
        curr, cost = queue.pop(0)
        if curr == end:
            continue
        
        for dir in range(4):
            front = (curr[0] + dr[dir], curr[1] + dc[dir])
            
            if grid[front[0]][front[1]] != '#' and memo[front[0]][front[1]] > cost:
                queue.append((front, cost + 1))
                memo[front[0]][front[1]] = cost + 1
            
    return

# Part One
def solve_part_one():        
    with open('input/day20.txt') as f:
        grid = f.read().splitlines()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'S':
                    start = (r, c)
                if grid[r][c] == 'E':
                    end = (r, c)
                    
        iterate(grid, start, end)
            
        ans = 0
        thres = 100
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid[0]) - 1):
                if grid[r][c] == '#':
                    if grid[r-1][c] != '#' and grid[r+1][c] != '#':
                        if abs(memo[r-1][c] - memo[r+1][c]) - 2 >= thres:
                            ans += 1
                    
                    if grid[r][c-1] != '#' and grid[r][c+1] != '#':
                        if abs(memo[r][c-1] - memo[r][c+1]) - 2 >= thres:
                            ans += 1
            

        print(f"Answer for part one: {ans}")

# Part Two
def solve_part_two():
    with open('input/day20.txt') as f:
        grid = f.read().splitlines()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'S':
                    start = (r, c)
                if grid[r][c] == 'E':
                    end = (r, c)
        
        iterate(grid, start, end)
        
        ans = 0
        thres = 100
        sv = {}
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid[0]) - 1):
                if grid[r][c] != '#':
                    for i in range(-20, 21):
                        for j in range(-20, 21):
                            if abs(i) + abs(j) <= 20 and r+i >= 0 and r+i < len(grid) and c+j >= 0 and c+j < len(grid[0]) and grid[r+i][c+j] != '#':
                                if memo[r+i][c+j] - memo[r][c] - abs(i) - abs(j) >= thres:
                                    if (memo[r+i][c+j] - memo[r][c] - abs(i) - abs(j)) not in sv:
                                        sv[memo[r+i][c+j] - memo[r][c] - abs(i) - abs(j)] = 0
                                    sv[memo[r+i][c+j] - memo[r][c] - abs(i) - abs(j)] += 1
                                    ans += 1
        
        print(f"Answer for part two: {ans}")
        
if __name__ == '__main__':
    solve_part_one()
    solve_part_two()