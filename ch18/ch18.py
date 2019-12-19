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

    def find(self, v):
        for y in range(self.min_height-1, self.height+1):
            for x in range(self.min_width-1, self.width+1):
                if (self.get((x,y)) == v):
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
    for x,c in enumerate(line):
        grid.put((x,y),c)

keys = {}
for c in string.ascii_lowercase:
    loc = grid.find(c)
    if (loc is not None):
        keys[c] = loc

lc = set(string.ascii_lowercase)
uc = set(string.ascii_uppercase)

from collections import defaultdict

global_seen = set()
def flood(start, node):
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
                flood(new_pos, mc)
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

graph = defaultdict(list)
start = grid.find('@')
flood(start, '@')
    
#for y in graph:
#    x = graph[y]
#    print(y, x)
#import sys; sys.exit()

seen = set()
q = []
v = (0,'@',frozenset(),[])
heappush(q, v)
while (len(q)):
    dist, mc, keys_collected, path = heappop(q) #q.pop(0)

    if ((mc, keys_collected) in seen):
        continue
    seen.add((mc, keys_collected))

    if (mc in lc and
        not mc in keys_collected):
        keys_collected = set(keys_collected)
        keys_collected.add(mc)
        keys_collected = frozenset(keys_collected)

        if (len(keys_collected) >= len(keys)):
            print("Done")
            print(dist)
            import sys; sys.exit()

    if (mc in uc and 
        not mc.lower() in keys_collected):
        continue

    for nmc in graph[mc]:
        v = (dist+nmc[1], nmc[0], keys_collected, path[:]+[nmc])
        heappush(q, v)
    #for nmc in graph[mc].parents:
    #    q.append((nmc[0], keys_collected, dist+nmc[1], path[:]+[nmc]))
    #print(q)

