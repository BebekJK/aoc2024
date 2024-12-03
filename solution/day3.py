def compute_sum(instruction):
    instruction = instruction.split('mul')
    instruction = [i for i in instruction if len(i) and i[0] == '(' and ')' in i]
    instruction = [i[1:].split(')')[0] for i in instruction]
    
    ans = 0
    for i in instruction:
        try:
            nums = i.split(',')
            num1, num2 = int(nums[0]), int(nums[1])
            ans += num1 * num2
        except:
            pass
    
    return ans

# Part One
def solve_part_one():
    with open('input/day3.txt') as f:
        data = f.read().splitlines()
        ans = 0
        for instruction in data:    
            ans += compute_sum(instruction)
        
        print(f"Answer for part one: {ans}")

# Part Two
def solve_part_two():
    with open('input/day3.txt') as f:
        data = f.read().splitlines()
        ans = 0
        do = True
        
        for instruction in data:
            prev = 0
            for i in range(len(instruction)):
                if instruction[i:i+4] == 'do()' and do == False:
                    prev = i+4
                    do = True
                elif instruction[i:i+7] == "don't()" and do == True:
                    ans += compute_sum(instruction[prev:i])
                    prev = i+6
                    do = False
            if do:
                ans += compute_sum(instruction[prev:])
        
        print(f"Answer for part two: {ans}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()