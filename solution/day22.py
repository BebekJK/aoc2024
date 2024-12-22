def split_line(line):
    return int(line)

def get_new_secret(num):
    op = 64 * num
    num = num ^ op
    num = num % (2 ** 24)
    op = num // 32
    num = num ^ op
    num = num % (2 ** 24)
    op = num * 2048
    num = num ^ op
    num = num % (2 ** 24)
    return num

# Part One
def solve_part_one():
    with open('input/day22.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        
        ans = 0
        for num in data:
            for _ in range(2000):
                num = get_new_secret(num)
            ans += num
        
        print(f"Answer for part one: {ans}")
        
# Part Two
def solve_part_two():
    with open('input/day22.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        
        prices = []
        for num in data:
            currprice = []
            for _ in range(2000):
                num = get_new_secret(num)
                currprice.append(num % 10)
            prices.append(currprice)
        
        diff = [[price[i+1] - price[i] for i in range(len(price)-1)] for price in prices]
        memo = {}
        
        for n, d in enumerate(diff):
            cons = []
            
            for i in range(len(d)):
                cons.append(d[i])
                if i < 3:
                    continue
                if tuple(cons) not in memo:
                    memo[tuple(cons)] = [-1 for i in range(len(diff))]
                    
                if memo[tuple(cons)][n] == -1:
                    memo[tuple(cons)][n] = prices[n][i+1]
                cons.pop(0)
        
        ans = 0
        for key in memo:
            s = [0 if d == -1 else d for d in memo[key]]
            if sum(s) > ans:
                ans = sum(s)
                
        print(f"Answer for part two: {ans}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()