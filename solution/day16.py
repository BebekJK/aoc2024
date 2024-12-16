memo = None
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def next_dir(dir):
    return (dir + 1) % 4

def prev_dir(dir):
    return (dir + 3) % 4

def reset(r, c):
    global memo
    memo = [[[10**6 for _ in range(4)] for _ in range(c)] for _ in range(r)]

def iterate(grid, start, end, dir):
    reset(len(grid), len(grid[0]))
    queue = []
    queue.append((start, dir, 0))
    minans  = 10**6
    
    while queue:
        curr, dir, cost = queue.pop(0)
        if curr == end:
            minans = min(minans, cost)
            continue
        
        front = (curr[0] + dr[dir], curr[1] + dc[dir])
        
        if grid[front[0]][front[1]] != '#' and memo[front[0]][front[1]][dir] > cost:
            queue.append((front, dir, cost + 1))
            memo[front[0]][front[1]][dir] = cost + 1
        
        if memo[curr[0]][curr[1]][prev_dir(dir)] > cost + 1000:
            queue.append((curr, prev_dir(dir), cost + 1000))
            memo[curr[0]][curr[1]][prev_dir(dir)] = cost + 1000

        if memo[curr[0]][curr[1]][next_dir(dir)] > cost + 1000:
            queue.append((curr, next_dir(dir), cost + 1000))
            memo[curr[0]][curr[1]][next_dir(dir)] = cost + 1000
            
    return minans

def backtrack(grid, start, end, dir, mincost):
    queue = []
    queue.append((end, dir, mincost))
    visited = set()
    while queue:
        curr, dir, cost = queue.pop(0)
        visited.add(curr)
        
        if curr == start:
            return len(visited)

        front = (curr[0] - dr[dir], curr[1] - dc[dir])
        
        if grid[front[0]][front[1]] != '#':
            if memo[front[0]][front[1]][dir] == cost - 1:
                queue.append((front, dir, cost - 1))
        
        if memo[curr[0]][curr[1]][prev_dir(dir)] == cost - 1000:
            queue.append((curr, prev_dir(dir), cost - 1000))

        if memo[curr[0]][curr[1]][next_dir(dir)] == cost - 1000:
            queue.append((curr, next_dir(dir), cost - 1000))
    
    return len(visited)

# Part One
def solve_part_one():        
    with open('input/day16.txt') as f:
        grid = f.read().splitlines()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'S':
                    start = (r, c)
                if grid[r][c] == 'E':
                    end = (r, c)
                    
        ans = iterate(grid, start, end, 1)
        print(f"Answer for part one: {ans}")

# Part Two
def solve_part_two():
    with open('input/day16.txt') as f:
        grid = f.read().splitlines()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 'S':
                    start = (r, c)
                if grid[r][c] == 'E':
                    end = (r, c)
        
        ans = iterate(grid, start, end, 1)
        lastdir = memo[end[0]][end[1]].index(ans)
        numtrack = backtrack(grid, start, end, lastdir, ans)
        print(f"Answer for part two: {numtrack}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()