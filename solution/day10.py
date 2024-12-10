def split_line(line):
    line = line.split(' ')
    return int(line[0]), int(line[-1])

# Part One
def solve_part_one():
    def bfs(data, src):
        vis = set()
        q = [src]
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        score = 0
        
        while len(q) > 0:
            r, c = q.pop(0)
            if (r, c) in vis:
                continue
            vis.add((r, c))
            
            if data[r][c] == '9':
                score += 1
                continue
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                if 0 <= nr < len(data) and 0 <= nc < len(data[0]) and data[nr][nc] != '.' and (int(data[nr][nc]) == int(data[r][c]) + 1):
                    q.append((nr, nc))
        
        return score
    
    with open('input/day10.txt') as f:
        data = f.read().splitlines()
        
        starts = []
        r, c = len(data), len(data[0])
        ans = 0
        
        for i in range(r):
            for j in range(c):
                if data[i][j] == '0':
                    starts.append((i, j))
        
        for start in starts:
            ans += bfs(data, start)
        print(f"Answer for part one: {ans}")

# Part Two
def solve_part_two():
    def bfs(data, starts):
        count = [[0 for __ in range(len(data[0]))] for _ in range(len(data))]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for start in starts:
            count[start[0]][start[1]] = 1
        
        for n in range(1,10):
            temp = [[0 for __ in range(len(data[0]))] for _ in range(len(data))]
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if data[i][j] == str(n):
                        for k in range(4):
                            ni, nj = i + dx[k], j + dy[k]
                            if 0 <= ni < len(data) and 0 <= nj < len(data[0]) and int(data[ni][nj]) == n - 1:
                                temp[i][j] += count[ni][nj]
            count = temp
        
        ans = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == '9':
                    ans += count[i][j]
                    
        return ans
    
    with open('input/day10.txt') as f:
        data = f.read().splitlines()
        
        starts = []
        r, c = len(data), len(data[0])
        ans = 0
        
        for i in range(r):
            for j in range(c):
                if data[i][j] == '0':
                    starts.append((i, j))
        
        ans = bfs(data, starts)
        print(f"Answer for part two: {ans}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()