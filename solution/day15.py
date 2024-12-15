# Part One
def solve_part_one():
    with open('input/day15.txt') as f:
        data = f.read().splitlines()
        breakline = data.index('')
        grid, move = data[:breakline], data[breakline+1:]
        move = ''.join(move)
        
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '@':
                    cr, cc = i, j
        
        
        for m in move:
            if m == '<':
                if  grid[cr][cc-1] == '#':
                    continue
                elif grid[cr][cc-1] == '.':
                    grid[cr] = grid[cr][:cc-1] + '@.' + grid[cr][cc+1:]
                    cc -= 1
                elif grid[cr][cc-1] == 'O':
                    length = 1
                    while grid[cr][cc-length] == 'O':
                        length += 1
                    if grid[cr][cc-length] == '#':
                        continue
                    # cc - length + 1 .. cc -> cc - length .. cc-1
                    grid[cr] = grid[cr][:cc-length] + grid[cr][cc-length+1:cc+1] + '.' + grid[cr][cc+1:]
                    cc -= 1
                
            elif m  == '>':
                if  grid[cr][cc+1] == '#':
                    continue
                elif grid[cr][cc+1] == '.':
                    grid[cr] = grid[cr][:cc] + '.@' + grid[cr][cc+2:]
                    cc += 1
                elif grid[cr][cc+1] == 'O':
                    length = 1
                    while grid[cr][cc+length] == 'O':
                        length += 1
                    if grid[cr][cc+length] == '#':
                        continue
                    # cc .. cc + length - 1 -> cc+1 .. cc+length
                    grid[cr] = grid[cr][:cc] + '.' + grid[cr][cc:cc+length] + grid[cr][cc+length+1:]
                    cc += 1
                    
            elif m == '^':
                if  grid[cr-1][cc] == '#':
                    continue
                elif grid[cr-1][cc] == '.':
                    grid[cr-1] = grid[cr-1][:cc] + '@' + grid[cr-1][cc+1:]
                    grid[cr] = grid[cr][:cc] + '.' + grid[cr][cc+1:]
                    cr -= 1
                elif grid[cr-1][cc] == 'O':
                    length = 1
                    while grid[cr-length][cc] == 'O':
                        length += 1
                    if grid[cr-length][cc] == '#':
                        continue
                    # cr - length + 1 .. cr -> cr - length .. cr - 1
                    for i in range(length, 0, -1):
                        grid[cr-i] = grid[cr-i][:cc] + grid[cr-i+1][cc] + grid[cr-i][cc+1:]
                    grid[cr] = grid[cr][:cc] + '.' + grid[cr][cc+1:]                        
                    cr -= 1
            else:
                if  grid[cr+1][cc] == '#':
                    continue
                elif grid[cr+1][cc] == '.':
                    grid[cr+1] = grid[cr+1][:cc] + '@' + grid[cr+1][cc+1:]
                    grid[cr] = grid[cr][:cc] + '.' + grid[cr][cc+1:]
                    cr += 1
                elif grid[cr+1][cc] == 'O':
                    length = 1
                    while grid[cr+length][cc] == 'O':
                        length += 1
                    if grid[cr+length][cc] == '#':
                        continue
                    # cr .. cr + length - 1 -> cr+1 .. cr+length
                    for i in range(length, 0, -1):
                        grid[cr+i] = grid[cr+i][:cc] + grid[cr+i-1][cc] + grid[cr+i][cc+1:]
                    grid[cr] = grid[cr][:cc] + '.' + grid[cr][cc+1:]                        
                    cr += 1
        
        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'O':
                    ans += 100 * i + j

        print("Answer for part one:", ans)
# Part Two
def solve_part_two():
    def get_points(grid, r, c, move):
        dr = 1 if move == 'v' else -1 if move == '^' else 0
        points = [(r, c)]
        if grid[r+dr][c] == '[':
            points += (get_points(grid, r+dr, c, move))
        elif grid[r+dr][c] == ']':
            points += (get_points(grid, r+dr, c-1, move))
        if grid[r+dr][c+1] == '[':
            points += (get_points(grid, r+dr, c+1, move))
        return points
        
        
    with open('input/day15.txt') as f:
        data = f.read().splitlines()
        breakline = data.index('')
        grid, move = data[:breakline], data[breakline+1:]
        move = ''.join(move)
        
        r, c = len(grid), len(grid[0])
        for i in range(r):
            nr = ''
            for j in range(c):
                if grid[i][j] == '#':
                    nr += '##'
                elif grid[i][j] == 'O':
                    nr += '[]'
                elif grid[i][j] == '@':
                    nr += '@.'
                else:
                    nr += '..'
            grid[i] = nr
        
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '@':
                    cr, cc = i, j
        
        
        for m in move:
            if m == '<':
                if  grid[cr][cc-1] == '#':
                    continue
                elif grid[cr][cc-1] == '.':
                    grid[cr] = grid[cr][:cc-1] + '@.' + grid[cr][cc+1:]
                    cc -= 1
                elif grid[cr][cc-1] == ']':
                    length = 1
                    while grid[cr][cc-length] == ']' or grid[cr][cc-length] == '[':
                        length += 1
                    if grid[cr][cc-length] == '#':
                        continue
                    # cc - length + 1 .. cc -> cc - length .. cc-1
                    grid[cr] = grid[cr][:cc-length] + grid[cr][cc-length+1:cc+1] + '.' + grid[cr][cc+1:]
                    cc -= 1
                
            elif m  == '>':
                if  grid[cr][cc+1] == '#':
                    continue
                elif grid[cr][cc+1] == '.':
                    grid[cr] = grid[cr][:cc] + '.@' + grid[cr][cc+2:]
                    cc += 1
                elif grid[cr][cc+1] == '[':
                    length = 1
                    while grid[cr][cc+length] == '[' or grid[cr][cc+length] == ']':
                        length += 1
                    if grid[cr][cc+length] == '#':
                        continue
                    # cc .. cc + length - 1 -> cc+1 .. cc+length
                    grid[cr] = grid[cr][:cc] + '.' + grid[cr][cc:cc+length] + grid[cr][cc+length+1:]
                    cc += 1
                    
            elif m == '^':
                if  grid[cr-1][cc] == '#':
                    continue
                elif grid[cr-1][cc] == '.':
                    grid[cr-1] = grid[cr-1][:cc] + '@' + grid[cr-1][cc+1:]
                    grid[cr] = grid[cr][:cc] + '.' + grid[cr][cc+1:]
                    cr -= 1
                elif grid[cr-1][cc] == '[' or grid[cr-1][cc] == ']':
                    if grid[cr-1][cc] == '[':
                        points = get_points(grid, cr-1, cc, '^')
                    else:
                        points = get_points(grid, cr-1, cc-1, '^')
                    
                    has_obs = sum([1 for p in points if grid[p[0]-1][p[1]] == '#' or grid[p[0]-1][p[1]+1] == '#']) > 0
                    if has_obs:
                        continue
                    else:
                        points.sort(key=lambda x: x[0])
                        for p in points:
                            grid[p[0]-1] = grid[p[0]-1][:p[1]] + '[]' + grid[p[0]-1][p[1]+2:]
                            grid[p[0]] = grid[p[0]][:p[1]] + '..' + grid[p[0]][p[1]+2:]
                        
                        grid[cr-1] = grid[cr-1][:cc] + '@' + grid[cr-1][cc+1:]
                        grid[cr] = grid[cr][:cc] + '.' + grid[cr][cc+1:]
                        cr -= 1
            else:
                if  grid[cr+1][cc] == '#':
                    continue
                elif grid[cr+1][cc] == '.':
                    grid[cr+1] = grid[cr+1][:cc] + '@' + grid[cr+1][cc+1:]
                    grid[cr] = grid[cr][:cc] + '.' + grid[cr][cc+1:]
                    cr += 1
                elif grid[cr+1][cc] == '[' or grid[cr+1][cc] == ']':
                    if grid[cr+1][cc] == '[':
                        points = get_points(grid, cr+1, cc, 'v')
                    else:
                        points = get_points(grid, cr+1, cc-1, 'v')
                    
                    has_obs = sum([1 for p in points if grid[p[0]+1][p[1]] == '#' or grid[p[0]+1][p[1]+1] == '#']) > 0
                    if has_obs:
                        continue
                    else:
                        points.sort(key=lambda x: x[0], reverse=True)
                        for p in points:
                            grid[p[0]+1] = grid[p[0]+1][:p[1]] + '[]' + grid[p[0]+1][p[1]+2:]
                            grid[p[0]] = grid[p[0]][:p[1]] + '..' + grid[p[0]][p[1]+2:]
                        
                        grid[cr+1] = grid[cr+1][:cc] + '@' + grid[cr+1][cc+1:]
                        grid[cr] = grid[cr][:cc] + '.' + grid[cr][cc+1:]
                        cr += 1
        

        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '[':
                    ans += 100 * i + j

        print("Answer for part two:", ans)


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()