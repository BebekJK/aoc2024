def split_line(line):
    line = line.split(':')
    
    if line[0] == 'Button A' or line[0] == 'Button B':
        move = line[1].strip().split(',')
        x = move[0].strip().split('+')[1]
        y = move[1].strip().split('+')[1]
        return int(x), int(y)
    else:
        move = line[1].strip().split(',')
        x = move[0].strip().split('=')[1]
        y = move[1].strip().split('=')[1]
        return int(x), int(y)

# Part One
def solve_part_one():
    with open('input/day13.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data if line != '']
        
        ans = 0
        for i in range(len(data)//3):
            ax, ay = data[3*i]
            bx, by = data[3*i+1]
            resx, resy = data[3*i+2]
            
            min_ans = 1e9
            for j in range(101):
                if (resx - ax * j) % bx == 0 and (resy - ay * j) % by == 0 and (resx - ax * j) // bx == (resy - ay * j) // by:
                    min_ans = min(min_ans, 3*j + (resx - ax * j) // bx)
            
            if min_ans != 1e9:
                ans += min_ans
        print(f"Answer for part one: {ans}")

# Part Two
def solve_part_two():
    with open('input/day13.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data if line != '']
        
        ans = 0
        for i in range(len(data)//3):
            ax, ay = data[3*i]
            bx, by = data[3*i+1]
            resx, resy = data[3*i+2]
            resx, resy = resx + 10000000000000, resy + 10000000000000
            
            det = ax * by - ay * bx
            if (by * resx - bx * resy) % abs(det) == 0 and (ax * resy - ay * resx) % abs(det) == 0:
                x = (by * resx - bx * resy) // det
                y = (ax * resy - ay * resx) // det
                if x >= 0 and y >= 0:
                    ans += 3*x + y
                
        print(f"Answer for part one: {ans}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()