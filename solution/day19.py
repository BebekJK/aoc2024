# Part One
memo = [-1 for _ in range(1000)]

def reset():
    global memo
    memo = [-1 for _ in range(1000)]
    
def dp(stripe, pos, colors, part):
    if pos == len(stripe):
        return 1
    
    if memo[pos] != -1:
        return memo[pos]
    
    ans = 0
    for color in colors:
        lc = len(color)
        if pos + lc <= len(stripe) and stripe[pos:pos + lc] == color:
            if part == 1:
                ans = dp(stripe, pos + lc, colors, part)
                if ans:
                    break
            else:
                ans += dp(stripe, pos + lc, colors, part)
    
    memo[pos] = ans
    return ans

def solve_part_one():
    with open('input/day19.txt') as f:
        data = f.read().splitlines()
        colors = data[0].split(',')
        colors = [color.strip() for color in colors]
        stripes = data[2:]
        
        ans = 0
        for stripe in stripes:
            reset()
            ans += dp(stripe, 0, colors, 1)
        
        print(f"Answer for part one: {ans}")

# Part Two
def solve_part_two():
    with open('input/day19.txt') as f:
        data = f.read().splitlines()
        colors = data[0].split(',')
        colors = [color.strip() for color in colors]
        stripes = data[2:]
        
        ans = 0
        for stripe in stripes:
            reset()
            ans += dp(stripe, 0, colors, 2)
        
        print(f"Answer for part one: {ans}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()