# Part One
def solve_part_one():
    def enc_lock(lock):
        l = lock[1:]
        l = [[c == '#' for c in r] for r in l]
        l = [sum([l[r][c] for r in range(6)]) for c in range(5)]
        return l
    
    def enc_key(key):
        k = key[:-1]
        k = [[c == '#' for c in r] for r in k]
        k = [sum([k[r][c] for r in range(6)]) for c in range(5)]
        return k
    
    with open('input/day25.txt') as f:
        data = f.read().splitlines()
        data = [line for line in data if line]
        
        data = [data[7*i:7*(i+1)] for i in range(len(data)//7)]
        locks = [line for line in data if line[0] == '#####']
        keys = [line for line in data if line[-1] == '#####']
        
        
        ans = 0
        
        for lock in locks:
            l = enc_lock(lock)
            for key in keys:
                k = enc_key(key)
                s = sum([l[i]+k[i] < 6 for i in range(5)])
                ans += (s == 5)
        
        
        print(f"Answer for part one: {ans}")
        
# Part Two
def solve_part_two():
    with open('input/day25.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        
        # print(f"Answer for part two: {ans}")

if __name__ == '__main__':
    solve_part_one()
    # solve_part_two()