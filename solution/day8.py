# Part One
def solve_part_one():    
    with open('input/day8.txt') as f:
        grid = f.read().splitlines()
        r, c = len(grid), len(grid[0])
        pos = {}
        ans = set()
        
        for row in grid:
            for col in row:
                if col == '.':
                    continue
                
                if col not in pos:
                    pos[col] = []
                pos[col].append((grid.index(row), row.index(col)))
        
        for key in pos:
            for i in range(len(pos[key])):
                for j in range(i+1, len(pos[key])):
                    lr, lc = pos[key][i]
                    rr, rc = pos[key][j]
                    dr, dc = rr - lr, rc - lc
                    
                    if lr - dr >= 0 and lr - dr < r and lc - dc >= 0 and lc - dc < c:
                        ans.add((lr - dr, lc - dc))
                    
                    if rr + dr >= 0 and rr + dr < r and rc + dc >= 0 and rc + dc < c:
                        ans.add((rr + dr, rc + dc))
        
        print(f"Answer for part one: {len(ans)}")
        
# Part Two
def solve_part_two():
    with open('input/day8.txt') as f:
        grid = f.read().splitlines()
        r, c = len(grid), len(grid[0])
        pos = {}
        ans = set()
        
        for row in grid:
            for col in row:
                if col == '.':
                    continue
                
                if col not in pos:
                    pos[col] = []
                pos[col].append((grid.index(row), row.index(col)))
        
        for key in pos:
            for i in range(len(pos[key])):
                for j in range(i+1, len(pos[key])):
                    lr, lc = pos[key][i]
                    rr, rc = pos[key][j]
                    dr, dc = rr - lr, rc - lc
                    
                    tempr, tempc = lr, lc
                    while(tempr >= 0 and tempr < r and tempc >= 0 and tempc < c):
                        ans.add((tempr, tempc))
                        tempr -= dr
                        tempc -= dc
                            
                    tempr, tempc = rr, rc
                    while(tempr >= 0 and tempr < r and tempc >= 0 and tempc < c):
                        ans.add((tempr, tempc))    
                        tempr += dr
                        tempc += dc
                          
        print(f"Answer for part two: {len(ans)}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()