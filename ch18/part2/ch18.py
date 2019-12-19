import string
from heapq import *
from collections import deque

class Grid:
    def __init__(self):
        self.grid = {}
        self.width = 1
        self.height = 1
        self.min_width = -1
        self.min_height = -1

    def put(self, pos, item):
        self.width = max(self.width, pos[0])
        self.height = max(self.height, pos[1])
        self.min_width = min(self.min_width, pos[0])
        self.min_height = min(self.min_height, pos[1])

        self.grid[pos] = item

    def get(self, pos):
        if (pos in self.grid):
            return self.grid[pos]
        return None

    def find(self, v, count=1):
        for y in range(self.min_height-1, self.height+1):
            for x in range(self.min_width-1, self.width+1):
                if (self.get((x,y)) == v):
                    count -= 1
                    if (count <= 0):
                        return (x,y)
        return None

    def draw(self):
        #print(chr(27)+'[2j')
        #print('\033c')
        #print('\x1bc')
        string = ''
        for y in range(self.min_height-1, self.height+1):
            for x in range(self.min_width-1, self.width+1):
                v = (x, y)
                vg = self.get(v)
                if (vg is not None):
                    string += vg
            string += '\n'
        print(string)

f = open('input.txt')
grid = Grid()
for y,line in enumerate(f):
    for x,c in enumerate(line.strip()):
        grid.put((x,y),c)

keys = {}
for c in string.ascii_lowercase:
    loc = grid.find(c)
    if (loc is not None):
        keys[c] = loc

lc = set(string.ascii_lowercase)
uc = set(string.ascii_uppercase)

from collections import defaultdict

def flood(start, node, graph):
    if (node in global_seen):
        return
    global_seen.add(node)

    seen = set()
    q = [(start,0)]
    while (len(q)):
        pos, dist = q.pop(0)
        if (pos in seen):
            continue
        seen.add(pos)

        for direction in [(0,1),(0,-1),(-1,0),(1,0)]:
            new_pos = (pos[0]+direction[0], pos[1]+direction[1])
            mc = grid.get(new_pos)
            if (mc == '#'):
                continue

            if ((mc in lc or mc in uc or mc == '@') and node != mc):
                graph[node].append((mc,dist+1))
                flood(new_pos, mc, graph)
                continue

            q.append((new_pos, dist+1))

def bfs(start, end):
    #print('a')
    #print(start)
    seen = set()
    q = [(start,0)]
    while (len(q)):
        pos, dist = q.pop(0)
        if (pos in seen):
            continue
        seen.add(pos)

        for direction in [(0,1),(0,-1),(-1,0),(1,0)]:
            new_pos = (pos[0]+direction[0], pos[1]+direction[1])
            if (new_pos == end):
                return dist+1

            mc = grid.get(new_pos)
            if (mc == '#'):
                continue
            q.append((new_pos, dist+1))

start = grid.find('@')
grid.put((start[0]-1,start[1]-1),'@')
grid.put((start[0],  start[1]-1),'#')
grid.put((start[0]+1,start[1]-1),'!')
grid.put((start[0]-1,start[1]),'#')
grid.put((start[0],  start[1]),'#')
grid.put((start[0]+1,start[1]),'#')
grid.put((start[0]-1,start[1]+1),'$')
grid.put((start[0]  ,start[1]+1),'#')
grid.put((start[0]+1,start[1]+1),'%')

global_seen = set()
start = grid.find('@')
graph1 = defaultdict(list)
flood(start, '@', graph1)

global_seen = set()
start = grid.find('!')
graph2 = defaultdict(list)
flood(start, '!', graph2)

global_seen = set()
start = grid.find('$')
graph3 = defaultdict(list)
flood(start, '$', graph3)

global_seen = set()
start = grid.find('%')
graph4 = defaultdict(list)
flood(start, '%', graph4)
    
#for y in graph1:
#    x = graph1[y]
#    print(y, x)
#for y in graph2:
#    x = graph2[y]
#    print(y, x)
#for y in graph3:
#    x = graph3[y]
#    print(y, x)
#for y in graph4:
#    x = graph4[y]
#    print(y, x)
#import sys; sys.exit()

seen = set()
q = []
v = (0,'@','!','$','%',frozenset(),[])
heappush(q, v)
while (len(q)):
    dist, mc1, mc2, mc3, mc4, keys_collected, path = heappop(q) #q.pop(0)

    if ((mc1, mc2, mc3, mc4, keys_collected) in seen):
        continue
    seen.add((mc1, mc2, mc3, mc4, keys_collected))

    if (mc1 in lc and
        not mc1 in keys_collected):
        keys_collected = set(keys_collected)
        keys_collected.add(mc1)
        keys_collected = frozenset(keys_collected)
    if (mc2 in lc and
        not mc2 in keys_collected):
        keys_collected = set(keys_collected)
        keys_collected.add(mc2)
        keys_collected = frozenset(keys_collected)
    if (mc3 in lc and
        not mc3 in keys_collected):
        keys_collected = set(keys_collected)
        keys_collected.add(mc3)
        keys_collected = frozenset(keys_collected)
    if (mc4 in lc and
        not mc4 in keys_collected):
        keys_collected = set(keys_collected)
        keys_collected.add(mc4)
        keys_collected = frozenset(keys_collected)

    if (len(keys_collected) >= len(keys)):
        print("Done")
        print(dist)
        import sys; sys.exit()

    if (mc1 in uc and 
        not mc1.lower() in keys_collected and 
        mc2 in uc and 
        not mc2.lower() in keys_collected and 
        mc3 in uc and 
        not mc3.lower() in keys_collected and 
        mc4 in uc and 
        not mc4.lower() in keys_collected):
        continue

    for nmc in graph1[mc1]:
        v = (dist+nmc[1], nmc[0], mc2, mc3, mc4, keys_collected, path[:]+[nmc])
        heappush(q, v)
    for nmc in graph2[mc2]:
        v = (dist+nmc[1], mc1, nmc[0], mc3, mc4, keys_collected, path[:]+[nmc])
        heappush(q, v)
    for nmc in graph3[mc3]:
        v = (dist+nmc[1], mc1, mc2, nmc[0], mc4, keys_collected, path[:]+[nmc])
        heappush(q, v)
    for nmc in graph4[mc4]:
        v = (dist+nmc[1], mc1, mc2, mc3, nmc[0], keys_collected, path[:]+[nmc])
        heappush(q, v)
    #for nmc in graph[mc].parents:
    #    q.append((nmc[0], keys_collected, dist+nmc[1], path[:]+[nmc]))
    #print(q)

