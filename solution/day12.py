visited = set()
points = []

# Part One
def solve_part_one():
    visited = set()
    def get_area(grid, x, y, reg):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        r, c = len(grid), len(grid[0])
        ans = 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if grid[nx][ny] == reg and (nx, ny) not in visited:
                visited.add((nx, ny))
                ans += get_area(grid, nx, ny, reg)
                points.append((nx, ny))
        
        return ans
            
    def get_perimeter():
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        perim = 0
        for point in points:
            x, y = point
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if (nx, ny) not in points:
                    perim += 1
        return perim
    
    with open('input/day12.txt') as f:
        grid = f.read().splitlines()
        r, c = len(grid), len(grid[0])
        
        ans = 0
        for i in range(r):
            for j in range(c):
                if (i, j) in visited:
                    continue
                
                global points
                visited.add((i, j))
                
                points = []
                points.append((i, j))
                ans += get_area(grid, i, j, grid[i][j]) * get_perimeter()
        
        
        print(f"Answer for part one: {ans}")

# Part Two
def solve_part_two():
    visited = set()
    def get_area(grid, x, y, reg):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        r, c = len(grid), len(grid[0])
        ans = 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if grid[nx][ny] == reg and (nx, ny) not in visited:
                visited.add((nx, ny))
                ans += get_area(grid, nx, ny, reg)
                points.append((nx, ny))
        
        return ans
            
    def get_sides():
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        sides = 0
        
        for i in range(4):
            side_vis = set()
            for point in points:
                if point in side_vis:
                    continue
                x, y = point
                nx, ny = x + dx[i], y + dy[i]
                
                if (nx, ny) not in points:
                    side_vis.add((x, y))
                    sides += 1
                    
                    if dy[i] == 0:
                        cnt = 0
                        while (x, y+cnt) in points and (nx, ny+cnt) not in points:
                            side_vis.add((x, y+cnt))
                            cnt += 1
                        cnt = 0
                        while (x, y-cnt) in points and (nx, ny-cnt) not in points:
                            side_vis.add((x, y-cnt))
                            cnt += 1
                    else:
                        cnt = 0
                        while (x+cnt, y) in points and (nx+cnt, ny) not in points:
                            side_vis.add((x+cnt, y))
                            cnt += 1
                        cnt = 0
                        while (x-cnt, y) in points and (nx-cnt, ny) not in points:
                            side_vis.add((x-cnt, y))
                            cnt += 1
        return sides
    
    with open('input/day12.txt') as f:
        grid = f.read().splitlines()
        r, c = len(grid), len(grid[0])
        
        ans = 0
        for i in range(r):
            for j in range(c):
                if (i, j) in visited:
                    continue
                
                global points
                visited.add((i, j))
                
                points = []
                points.append((i, j))
                ans += get_area(grid, i, j, grid[i][j]) * get_sides()
        
        
        print(f"Answer for part two: {ans}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()