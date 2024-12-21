import sys
sys.setrecursionlimit(10 ** 6)
# Part One
moverob = {
    0: [None, None, 2, 4],
    1: [None, None, None, 2],
    2: [0, 1, None, 3],
    3: [4, 2, None, None],
    4: [None, 0, 3, None]
}

movekey = {
    0: [2, None, None, 10],
    1: [4, None, None, 2],
    2: [5, 1, 0, 3],
    3: [6, 2, 10, None],
    4: [7, None, 1, 5],
    5: [8, 4, 2, 6],
    6: [9, 5, 3, None],
    7: [None, None, 4, 8],
    8: [None, 7, 5, 9],
    9: [None, 8, 6, None],
    10: [3, 0, None, None]
}

move = [
    [[], [[(0, 2), (2, 1)]], [[(0, 2)]], [[(0, 2), (2, 3)], [(0, 4), (4, 3)]], [[(0, 4)]]],
    [[[(1, 2), (2, 0)]], [], [[(1, 2)]], [[(1, 2), (2, 3)]], [[(1, 2), (2, 3), (3, 4)], [(1, 2), (2, 0), (0, 4)]]],
    [[[(2, 0)]], [[(2, 1)]], [], [[(2, 3)]], [[(2, 0), (0, 4)], [(2, 3), (3, 4)]]],
    [[[(3, 4), (4, 0)], [(3, 2), (2, 0)]], [[(3, 2), (2, 1)]], [[(3, 2)]], [], [[(3, 4)]]],
    [[[(4, 0)]], [[(4, 0), (0, 2), (2, 1)], [(4, 3), (3, 2), (2, 1)]], [[(4, 3), (3, 2)], [(4, 0), (0, 2)]], [[(4, 3)]], []],
]

nummove = [
    [1, 3, 2, 3, 2],
    [3, 1, 2, 3, 4],
    [2, 2, 1, 2, 3],
    [3, 3, 2, 1, 2],
    [2, 4, 3, 2, 1]
]

moveid = [
    [-1, -1, 2, -1,  3],
    [-1, -1, 3, -1, -1],
    [0, 1, -1, 3, -1],
    [-1, -1, 1, -1, 0],
    [1, -1, -1, 2, -1],
]
def solve_part_one():
    def solve(state1, state2, state3, word, target):
        visited = set() 
        queue = [(state1, state2, state3, word, 0)]
        visited.add((state1, state2, state3, word))
        
        while queue:
            state1, state2, state3, word, movelen = queue.pop(0)
            
            if word == target:
                return movelen

            if len(word) != 0 and not target.startswith(word):
                continue

            for i in range(5):
                if i == 4:
                    if state1 == 4 and state2 == 4:
                        if (state1, state2, state3, word + ("A" if state3 == 10 else str(state3))) not in visited:
                            queue.append((state1, state2, state3, word + ("A" if state3 == 10 else str(state3)), movelen+1))
                            visited.add((state1, state2, state3, word + ("A" if state3 == 10 else str(state3))))
                    elif state1 == 4:
                        if movekey[state3][state2] is not None:
                            if (state1, state2, movekey[state3][state2], word) not in visited:
                                queue.append((state1, state2, movekey[state3][state2], word, movelen+1))
                                visited.add((state1, state2, movekey[state3][state2], word))
                    else:
                        if moverob[state2][state1] is not None:
                            if (state1, moverob[state2][state1], state3, word) not in visited:
                                queue.append((state1, moverob[state2][state1], state3, word, movelen+1))
                                visited.add((state1, moverob[state2][state1], state3, word))
                elif moverob[state1][i] is not None:
                    if (moverob[state1][i], state2, state3, word) not in visited:
                        queue.append((moverob[state1][i], state2, state3, word, movelen+1))
                        visited.add((moverob[state1][i], state2, state3, word))
        
        return -1
    
    with open('input/day21.txt') as f:
        data = f.read().splitlines()
        
        ans = 0
        for line in data:
            ans += solve(4, 4, 10, "", line) * int(line[:3])
            
        
        print(f"Answer for part one: {ans}")
        
# Part Two
def solve_part_two():
    def get_state_id(states):
        return sum([states[i] * (5 ** i) * 100 if i != len(states)-1 else states[i] for i in range(len(states))])
    
    def solve(states, word, target):
        visited = set() 
        queue = [(states, word, "4")]
        visited.add((get_state_id(states), word))
        
        while queue:
            states, word, move = queue.pop(0)
            curr = states.copy()
            if word == target:
                # print(move, len(move))
                return move

            if len(word) != 0 and not target.startswith(word):
                continue

            for i in range(5):
                if i == 4:
                    proc = False
                    for j in range(len(curr)-1, -1, -1):
                        if sum(curr[:j]) == 4*j:
                            proc = True
                            if j == len(curr)-1:
                                next_word = word + ("A" if curr[j] == 10 else str(curr[j]))
                                if (get_state_id(curr), next_word) not in visited:
                                    queue.append((curr, next_word, move + "4"))
                                    visited.add((get_state_id(curr), next_word))
                            elif j == len(curr)-2:
                                if movekey[curr[j+1]][curr[j]] is not None:
                                    next_word = word
                                    if (get_state_id(curr[:j+1]+[movekey[curr[j+1]][curr[j]]]), next_word) not in visited:
                                        queue.append((curr[:j+1]+[movekey[curr[j+1]][curr[j]]], next_word, move + str(curr[j])))
                                        visited.add((get_state_id(curr[:j+1]+[movekey[curr[j+1]][curr[j]]]), next_word))
                            else:
                                if moverob[curr[j+1]][curr[j]] is not None:
                                    next_word = word
                                    if (get_state_id(curr[:j+1]+[moverob[curr[j+1]][curr[j]]]+curr[j+2:]), next_word) not in visited:
                                        queue.append((curr[:j+1]+[moverob[curr[j+1]][curr[j]]]+curr[j+2:], next_word, move))
                                        visited.add((get_state_id(curr[:j+1]+[moverob[curr[j+1]][curr[j]]]+curr[j+2:]), next_word))
                        if proc:
                            break
                    
                elif moverob[curr[0]][i] is not None:
                    if (get_state_id([moverob[curr[0]][i]] + curr[1:]), word) not in visited:
                        queue.append(([moverob[curr[0]][i]] + curr[1:], word, move))
                        visited.add((get_state_id([moverob[curr[0]][i]] + curr[1:]), word))
        
        return -1
    
    with open('input/day21.txt') as f:
        data = f.read().splitlines()
        
        ans = 0
        global nummove
        
        for _ in range(24):
            newmove = [[1 for _ in range(5)] for _ in range(5)]
            for i in range(5):
                for j in range(5):
                    mincost = 10**12
                    for mls in move[i][j]:
                        if len(mls) > 0:
                            prev = moveid[mls[0][0]][mls[0][1]]
                            cost = nummove[4][prev]
                            for m in mls[1:]:
                                curr = moveid[m[0]][m[1]]
                                cost += nummove[prev][curr]
                                prev = curr
                            cost += nummove[prev][4]
                            mincost = min(cost, mincost)
                    
                    newmove[i][j] = mincost if mincost != 10**12 else 1
            nummove = newmove
            
        for line in data:
            mv = solve([4, 4, 10], "", line)
            cost = 0
            for i in range(len(mv)-1):
                cost += newmove[int(mv[i])][int(mv[i+1])]
            ans += cost * int(line[:3])
        print(f"Answer for part two: {ans}")

if __name__ == '__main__':
    # solve_part_one()
    solve_part_two()