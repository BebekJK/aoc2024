def split_line(line):
    line = line.split(',')
    return int(line[1]), int(line[0])

def rep(string, pos, char):
    return string[:pos] + char + string[pos + 1:]

def bfs(grid, start, end):
    q = [(start[0], start[1], 0)]
    visited = set()
    visited.add(start)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while q:
        r, c, d = q.pop(0)
        if (r, c) == end:
            return d
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '.' and (nr, nc) not in visited:
                q.append((nr, nc, d + 1))
                visited.add((nr, nc))
    return -1

# Part One
def solve_part_one():
    with open('input/day18.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        r, c = 71, 71
        n = 1024
        
        grid = ['.' * c for _ in range(r)]
        for i, (x, y) in enumerate(data):
            if i == n:
                break
            grid[x] = rep(grid[x], y, '#')
        
        ans = bfs(grid, (0,0), (r-1,c-1))
        print(f"Answer for part one: {ans}")

# Part Two
def solve_part_two():
    with open('input/day18.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        r, c = 71, 71
        
        le, ri, save = 0, len(data)-1, -1
        while le <= ri:
            n = (le + ri) // 2
            grid = ['.' * c for _ in range(r)]
            for i, (x, y) in enumerate(data):
                if i == n:
                    break
                grid[x] = rep(grid[x], y, '#')
            
            ans = bfs(grid, (0,0), (r-1,c-1))
            if ans == -1:
                save = n
                ri = n - 1
            else:
                le = n + 1
        print(f"Answer for part two: {data[save-1][1]},{data[save-1][0]}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()