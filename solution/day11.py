def split_line(line):
    line = line.split(' ')
    return line

# Part One
def solve_part_one():
    def next_blink(curr):
        tmp = []
        for n in curr:
            if n == '0':
                tmp.append('1') 
            elif len(n) % 2 == 0:
                tmp.append(str(int(n[:len(n)//2])))
                tmp.append(str(int(n[len(n)//2:])))
            else:
                tmp.append(str(int(n)*2024))
            
        return tmp
    
    with open('input/day11.txt') as f:
        data = f.read().splitlines()
        data = split_line(data[0])
        for _ in range(25):
            data = next_blink(data)
        print(f"Answer for part one: {len(data)}")

# Part Two
def solve_part_two():
    def next_blink(curr):
        tmp = {}
        for n in curr:
            if n == '0':
                if '1' in tmp:
                    tmp['1'] += curr[n]
                else:
                    tmp['1'] = curr[n]
            
            elif len(n) % 2 == 0:
                left = str(int(n[:len(n)//2]))
                right = str(int(n[len(n)//2:]))
                
                if left in tmp:
                    tmp[left] += curr[n]
                else:
                    tmp[left] = curr[n]
                
                if right in tmp:
                    tmp[right] += curr[n]
                else:
                    tmp[right] = curr[n]
            
            else:
                nx = str(int(n)*2024)
                if nx in tmp:
                    tmp[nx] += curr[n]
                else:
                    tmp[nx] = curr[n]
                
        return tmp
    
    with open('input/day11.txt') as f:
        data = f.read().splitlines()
        data = split_line(data[0])
        tmp = {}
        for n in data:
            if n in tmp:
                tmp[n] += 1
            else:
                tmp[n] = 1
        data = tmp
        
        for _ in range(75):
            data = next_blink(data)
        ans = 0
        for n in data:
            ans += data[n]
        print(f"Answer for part two: {ans}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()