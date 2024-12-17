def split_line(line):
    if line == '':
        return
    if 'A' in line or 'B' in line or 'C' in line:
        return int(line.split(':')[1].strip())
    
    return [int(x) for x in line.split(':')[1].strip().split(',')]

# Part One
def solve_part_one():
    with open('input/day17.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        a, b, c = data[0], data[1], data[2]
        ops = data[4]
        output = []
        ptr = 0
        
        while ptr < len(ops):
            op, val = ops[ptr], ops[ptr+1]
            val = a if val == 4 else b if val == 5 else c if val == 6 else val
            if op == 0:
                a = a // (2 ** val)
            elif op == 1:
                b = b ^ val
            elif op == 2:
                b = val % 8
            elif op == 3:
                if a != 0:
                    ptr = val
                    continue
            elif op == 4:
                b = b ^ c
            elif op == 5:
                output.append(val%8)
            elif op == 6:
                b = a // (2 ** val)
            elif op == 7:
                c = a // (2 ** val)
                
            ptr += 2

        print(f"Answer for part one: {','.join(map(str, output))}")
            
            
                 
        
        # print(f"Answer for part one: {dist}")

# Part Two
def solve_part_two():
    ans = []
    
    def get_output(val, ops):
        a, b, c = sum([v * (8**i) for i, v in enumerate(val)]), 0, 0
        output = []
        ptr = 0
        
        while ptr < len(ops):
            op, val = ops[ptr], ops[ptr+1]
            val = a if val == 4 else b if val == 5 else c if val == 6 else val
            if op == 0:
                a = a // (2 ** val)
            elif op == 1:
                b = b ^ val
            elif op == 2:
                b = val % 8
            elif op == 3:
                if a != 0:
                    ptr = val
                    continue
            elif op == 4:
                b = b ^ c
            elif op == 5:
                output.append(val%8)
            elif op == 6:
                b = a // (2 ** val)
            elif op == 7:
                c = a // (2 ** val)
            
            ptr += 2
        
        return output
    
    def recur(currpow, pos, ops):
        if pos == 15:
            val = sum([v * (8**i) for i, v in enumerate(currpow)])
            output = get_output(currpow, ops)
            if len(output) == 16:
                ans.append(val)
            return
        
        if pos == 0:
            for p in [[i//512, i//64 % 8, i//8 % 8, i%8]for i in range(4096)]:
                output = get_output(p, ops)
                if output[pos] == ops[pos]:
                    recur(p, pos+1, ops)
        else:
            for i in range(8):
                pc = currpow + [i]
                output = get_output(pc, ops)
                if len(output) <= pos:
                    continue
                if output[pos] == ops[pos]:
                    recur(pc, pos+1, ops)
            
                
    with open('input/day17.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        ops = data[4]
        recur([], 0, ops)
        print(f"Answer for part two: {min(ans)}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()