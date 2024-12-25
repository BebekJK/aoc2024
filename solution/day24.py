import random

nodes = {}

def split_line(line):
    if line == '':
        return None
    
    if ':' in line:
        line = line.split(':')
        return line[0], 1 if line[1].strip() == '1' else 0
    
    line = line.split(' ')
    return line[0], line[1], line[2], line[4]

# Part One
def solve_part_one():
    with open('input/day24.txt') as f:
        data = f.read().splitlines()
        data = [split_line(line) for line in data]
        data = [line for line in data if line]
        
        num_node = 90
        node_data, adj_data = data[:num_node], data[num_node:]
        words = {}
        
        for line in node_data:
            nodes[line[0]] = line[1]
            words[line[0]] = str(line[1])
            
        count = 0
        visited = [0 for _ in range(len(adj_data))]
        
        while count < len(adj_data):
            for i, adj in enumerate(adj_data):
                if visited[i]:
                    continue
                
                if adj[0] in nodes and adj[2] in nodes:
                    visited[i] = 1
                    count += 1
                    
                    if adj[1] == 'AND':
                        nodes[adj[3]] = nodes[adj[0]] & nodes[adj[2]]
                    elif adj[1] == 'OR':
                        nodes[adj[3]] = nodes[adj[0]] | nodes[adj[2]]
                    elif adj[1] == 'XOR':
                        nodes[adj[3]] = nodes[adj[0]] ^ nodes[adj[2]]
                    
                    words[adj[3]] = f'({words[adj[0]]} {adj[1]} {words[adj[2]]})'
        
        ans = sorted(list(nodes.keys()))
        ans = [nodes[key] for key in ans if key[0] == 'z']
        ans = sum([2**i for i, val in enumerate(ans) if val])
        
        # for key, val in words.items():
        #     if key[0] == 'z':
        #         print(f"{key}: {val}")  
        print(f"Answer for part one: {ans}")
        
# Part Two
def solve_part_two():
    ## idk ?
    pass

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()