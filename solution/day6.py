# Part One
def solve_part_one():
    with open('input/day6.txt') as f:
        grid = f.read().splitlines()
        r, c = len(grid), len(grid[0])
        cr, cc = -1, -1
        for row in grid:
            if '^' in row:
                cr = grid.index(row)
                cc = row.index('^')
                break
        
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        cdir = 0
        while True:
            nr = cr + dirs[cdir][0]
            nc = cc + dirs[cdir][1]
            
            if nr < 0 or nr >= r or nc < 0 or nc >= c:
                break
            
            if grid[nr][nc] == '#':
                cdir = (cdir + 1) % 4
            else:
                grid[cr] = grid[cr][:cc] + 'X' + grid[cr][cc+1:]
                cr, cc = nr, nc
                
        ans = 1
        for row in grid:
            ans += row.count('X')
        
        print(f"Answer for part one: {ans}")

# Part Two
def solve_part_two():
    def check_loop(cr, cc, grid):
        count = 0
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        cdir = 0
        
        while True:
            nr = cr + dirs[cdir][0]
            nc = cc + dirs[cdir][1]
            
            if nr < 0 or nr >= r or nc < 0 or nc >= c:
                break
            
            if grid[nr][nc] == '#':
                cdir = (cdir + 1) % 4
            else:
                cr, cc = nr, nc
                count += 1

            if count > 10000:
                return True
        return False
    
    with open('input/day6.txt') as f:
        grid = f.read().splitlines()
        r, c = len(grid), len(grid[0])
        cr, cc = -1, -1
        tempr, tempc = -1, -1
        for row in grid:
            if '^' in row:
                cr = grid.index(row)
                cc = row.index('^')
                tempr, tempc = cr, cc
                break
        
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        cdir = 0
        check = set()
        check.add((cr, cc))
        
        while True:
            nr = cr + dirs[cdir][0]
            nc = cc + dirs[cdir][1]
            
            if nr < 0 or nr >= r or nc < 0 or nc >= c:
                break
            
            if grid[nr][nc] == '#':
                cdir = (cdir + 1) % 4
            else:
                check.add((nr, nc))
                cr, cc = nr, nc
        
        ans = 0
        for item in check:
            cr, cc = tempr, tempc
            grid[item[0]] = grid[item[0]][:item[1]] + '#' + grid[item[0]][item[1]+1:]
            if check_loop(cr, cc, grid):
               ans += 1 
            grid[item[0]] = grid[item[0]][:item[1]] + '.' + grid[item[0]][item[1]+1:]

        print(f"Answer for part two: {ans}")
        
if __name__ == '__main__':
    solve_part_one()
    solve_part_two()