from collections import defaultdict

graph = defaultdict(list)
graphp = defaultdict(list)
for line in open('input.txt'):
    line = line.strip()
    if (not line):
        break
    line = line.split(')')
    graph[line[0]].append(line[1])
    graphp[line[1]].append(line[0])

seen = {}
stack = [('YOU',0)]
while stack:
    node,depth = stack.pop(0)
    #print(node, stack)
    if (node in seen):
        continue
    seen[node] = True

    if (node == 'SAN'):
        print("SAN",depth)
        break

    # Explore children
    for n in graph[node]:
        stack.append((n,depth+1))

    # Explore parent
    for n in graphp[node]:
        stack.append((n,depth+1))

