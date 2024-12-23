adj = {}

def split_line(line):
    line = line.split('-')
    return line[0], line[1]

# Part One
def solve_part_one():
    with open('input/day23.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        
        for d in data:
            idx0, idx1 = d[0], d[1]
            if idx0 not in adj:
                adj[idx0] = []
            adj[idx0].append(idx1)
            
            if idx1 not in adj:
                adj[idx1] = []
            adj[idx1].append(idx0)
        
        ans = 0
        for key1 in adj:
            for key2 in adj[key1]:
                for key3 in adj[key2]:
                    if key3 in adj[key1] and (key1[0] == 't' or key2[0] == 't' or key3[0] == 't'):
                        ans += 1
        
        ans //= 6
        print(f"Answer for part one: {ans}")
        
# Part Two
def solve_part_two():
    def bfs(nodes):
        
        q = [','.join([node]) for node in nodes]
        lg, seq = 0, ""
        
        while q:
            curr = q.pop(0).split(',')
            last = nodes.index(curr[-1])
            
            if len(curr) > lg:
                lg = len(curr)
                seq = curr
                
            for i in range(last+1, len(nodes)):
                exist = sum([nodes[i] in adj[node] for node in curr])
                if exist != len(curr):
                    continue
                q.append(','.join(curr + [nodes[i]]))
        
        return ','.join(seq)
    
    with open('input/day23.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        
        ans = bfs(sorted(list(adj.keys())))
        
        print(f"Answer for part two: {ans}")

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()