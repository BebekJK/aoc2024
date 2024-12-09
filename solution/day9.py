# Part One
def solve_part_one():    
    with open('input/day9.txt') as f:
        data = f.read().splitlines()[0]
        
        num = [int(num) for i, num in enumerate(data) if i%2 == 0]
        num = list(zip(num, range(len(num))))
        
        ans = 0
        cnt = 0
        ptr = len(num) -1 
        mx = sum([i[0] for i in num])
        for i in range(len(data)):
            if i%2 == 0:
                for _ in range(int(data[i])):
                    if(mx == cnt): break
                    ans += (i//2) * cnt
                    cnt += 1
                continue
            
            if(mx == cnt): break
            
            for _ in range(int(data[i])):
                if(mx == cnt): break
                ans += cnt * num[ptr][1]
                cnt += 1
                
                if(num[ptr][0] > 1):
                    num[ptr] = (num[ptr][0]-1, num[ptr][1])
                else:
                    ptr -= 1
            
        print(f"Answer for part one: {ans}")
        
# Part Two
def solve_part_two():
    with open('input/day9.txt') as f:
        data = f.read().splitlines()[0]
        
        num, skip = [int(num) for i, num in enumerate(data) if i%2 == 0], [int(num) for i, num in enumerate(data) if i%2 == 1]
        num = list(zip(num, range(len(num))))
        pos = []
        ans = 0
        for i in range(len(num)-1, -1, -1):
            sz = num[i][0]
            for j, s in enumerate(skip):
                if i < j: break
                if s >= sz:
                    skip[j] -= sz
                    pos.append((num[i][1], j, sz))
                    break
        
        pos = sorted(pos, key=lambda x: x[1])
        moved = [False] * len(num)
        for n, _, __ in pos:
            moved[n] = True
        
        cnt = 0
        ptrp = 0
        for i, n in enumerate(data):
            if i % 2 == 0:
                if not moved[i//2]:
                    for j in range(int(n)):
                        ans += (i//2) * cnt
                        print(f"Adding {i//2} * {cnt} to answer")
                        cnt += 1
                else:
                    cnt += int(n)
            else:
                if ptrp < len(pos) and pos[ptrp][1] == i//2:
                    slot = int(n)
                    while(pos[ptrp][1] == i//2):
                        for j in range(pos[ptrp][2]):
                            ans += cnt * pos[ptrp][0]
                            print(f"Adding {pos[ptrp][0]} * {cnt} to answer")
                            cnt += 1
                            slot -= 1
                        ptrp += 1
                        if ptrp == len(pos): break
                    
                    cnt += slot
                else:
                    cnt += int(n)
        print(f"Answer for part two: {ans}")

if __name__ == '__main__':
    # solve_part_one()
    solve_part_two()