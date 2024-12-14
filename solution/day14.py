def split_line(line):
    line = line.split(' ')
    pos = line[0].split('=')[1].split(',')
    pos = [int(pos[1]), int(pos[0])]
    v = line[1].split('=')[1].split(',')
    v = [int(v[1]), int(v[0])]
    return pos, v

# Part One
def solve_part_one():
    with open('input/day14.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        
        r, c = 103,101
        time = 100
        
        data = [((pos[0] + v[0] * time, pos[1] + v[1] * time), v) for pos, v in data]
        data = [((pos[0] % r + r) % r, (pos[1] % c + c) % c) for pos, v in data]
        
        q1 = sum(pos[0] > r // 2 and pos[1] > c // 2 for pos in data)
        q2 = sum(pos[0] > r // 2 and pos[1] < c // 2 for pos in data)
        q3 = sum(pos[0] < r // 2 and pos[1] > c // 2 for pos in data)
        q4 = sum(pos[0] < r // 2 and pos[1] < c // 2 for pos in data)
        
        print(f"Answer for part one: {q1 * q2 * q3 * q4}")
        # print(f"Answer for part one: {dist}")

# Part Two
def solve_part_two():
    with open('input/day14.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        
        r, c = 103,101
        time = 10000
        with open(f'out.txt', 'w') as fo:
            for i in range(time):
                data = [((pos[0] + v[0], pos[1] + v[1]), v) for pos, v in data]
                data = [([(pos[0] % r + r) % r, (pos[1] % c + c) % c], v) for pos, v in data]
                
                grid = [['.' for _ in range(c)] for _ in range(r)]
                for pos, _ in data:
                    grid[pos[0]][pos[1]] = '#'
                
                if (i % 101) == 10:
                    fo.write('\n' + 'Iteration ' + str(i) + '\n')
                    fo.write('\n'.join(''.join(row) for row in grid))
        print(f"Answer for part two: 7687")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()