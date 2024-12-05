blank = False

def split_line(line):
    global blank
    if blank:
        return split_order(line)
    
    if line == '':
        blank = True
        return None
    
    return split_rules(line)

def split_rules(line):
    line = line.split('|')
    return int(line[0]), int(line[-1])

def split_order(line):
    line = line.split(',')
    return [int(i) for i in line]

# Part One
def solve_part_one():
    global blank
    blank = False
    
    with open('input/day5.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        
        rules = [line for line in data if line is not None and type(line) is tuple]
        instructions = [line for line in data if line is not None and type(line) is list]
        ans = 0
        
        for instruction in instructions:
            valid = True
            for rule in rules:
                num1, num2 = rule
                try:
                    idx1, idx2 = instruction.index(num1), instruction.index(num2)
                    valid = valid and (idx1 < idx2)
                except:
                    continue
                if not valid:
                    break
                
            if valid:
                ans += instruction[len(instruction)//2]
                
        print(f"Answer for part one: {ans}")

# Part Two
def solve_part_two():
    global blank
    blank = False
    
    def fix_order(order, rules):
        for i in range(len(order)):
            for j in range(i+1, len(order)):
                if (order[j], order[i]) in rules:
                    order[i], order[j] = order[j], order[i]
        
        return order
    with open('input/day5.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        
        rules = [line for line in data if line is not None and type(line) is tuple]
        instructions = [line for line in data if line is not None and type(line) is list]
        ans = 0
        
        for instruction in instructions:
            valid = True
            for rule in rules:
                num1, num2 = rule
                try:
                    idx1, idx2 = instruction.index(num1), instruction.index(num2)
                    valid = valid and (idx1 < idx2)
                except:
                    continue
                if not valid:
                    break
                
            if not valid:
                fix_order(instruction, rules)
                ans += instruction[len(instruction)//2]
        
        print(f"Answer for part two: {ans}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()