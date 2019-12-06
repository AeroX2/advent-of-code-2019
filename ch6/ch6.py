from collections import defaultdict

graph = defaultdict(list)
for line in open('input.txt'):
    line = line.strip()
    if (not line):
        break
    line = line.split(')')
    print(line)
    graph[line[0]].append(line[1])

def dfs(base, depth=0):
    count = depth
    for node in graph[base]:
        count += dfs(node, depth+1)
    return count


print(dfs('COM'))
