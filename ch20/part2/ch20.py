import string
from heapq import *
from collections import defaultdict

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
        return ''

    def find(self, v, count=1):
        for y in range(self.min_height-1, self.height+1):
            for x in range(self.min_width-1, self.width+1):
                if (self.get((x,y)) == v):
                    count -= 1
                    if (count <= 0):
                        return (x,y)
        return None

    def iterate(self, fn):
        for y in range(self.min_height-1, self.height+1):
            for x in range(self.min_width-1, self.width+1):
                fn((x,y))

    def draw(self):
        #print(chr(27)+'[2j')
        #print('\033c')
        #print('\x1bc')
        string = ''
        for y in range(self.min_height-1, self.height+1):
            for x in range(self.min_width-1, self.width+1):
                v = (x, y)
                vg = self.get(v)
                if (vg != ''):
                    string += vg
            string += '\n'
        print(string)


global_seen = set()
def flood(start, teleporter):
    #print(start, teleporter)
    if (start in global_seen):
        return
    global_seen.add(start)
    #print("Going ahead")

    q = []
    seen = set()
    heappush(q, (0,start))
    while (len(q)):
        dist, pos = heappop(q)

        if (pos in seen):
            continue
        seen.add(pos)

        for direction in [(0,1),(0,-1),(-1,0),(1,0)]:
            new_pos = (pos[0]+direction[0], pos[1]+direction[1])
            mc = grid.get(new_pos)
            if (mc == '#'):
                continue
            if (mc == ''):
                continue
            if (mc == ' '):
                continue

            v = is_teleporter_entrance(new_pos)
            if (v[0] and v[1] != teleporter):
                graph[teleporter+("Outer" if is_outer(grid,start) else "Inner")].append((v[1]+("Outer" if is_outer(grid,pos) else "Inner"),dist+1,))
                flood(pos, v[1])
                
                l = teleporters[teleporter]
                for p in l:
                    if (p != start):
                        flood(p, teleporter)
                continue

            heappush(q, (dist+1, new_pos))

def bfs(start, end):
    #seen = set()

    q = []
    v = (0,0,start,[])
    heappush(q, v)
    while (len(q)):
        #print(q)
        #print(list([x[3] for x in q if len(x[3])>0 and x[3][0][0] == 'XFInner']))
        #print(list([x[3] for x in q if len(x[3])>0 and x[3][0] == 'XFInner']))
        dist, depth, mc, path = heappop(q) #q.pop(0)
        #print(mc)
        #print(graph[mc])

        if (mc[:2] == end[:2] and depth == 1):
            print(path)
            print(sum(map(lambda x: x[0][1], path))-1)
            break

        if (mc[:2] == end[:2]):
            continue

        #if (mc in seen):
        #    print("Continue")
        #    continue
        #print("Add",mc)
        #seen.add(mc)

        for nmc in graph[mc]:
            portal, odist = nmc

            d = -1 if portal[2:] == "Inner" else 1
            opp = "Inner" if portal[2:] == "Outer" else "Outer"

            if (depth+d <= 1):
                v = (dist+odist, depth+d, portal[:2]+opp, path[:]+[(nmc,depth)])
                heappush(q, v)
        #print(q)

def is_teleporter_entrance(pos):
    vg = grid.get(pos)
    if (vg not in string.ascii_uppercase):
        return (False,)

    upi = (pos[0],pos[1]+1)
    downi = (pos[0],pos[1]-1)
    lefti = (pos[0]-1,pos[1])
    righti = (pos[0]+1,pos[1])

    up = grid.get(upi)
    down = grid.get(downi)
    left = grid.get(lefti)
    right = grid.get(righti)

    vf = None
    final = vg
    direction_to_check = None
    if (up in uc):
        vf = up
        final = final+vf
        direction_to_check = downi
    elif (down in uc):
        vf = down
        final = vf+final
        direction_to_check = upi
    elif (left in uc):
        vf = left
        final = vf+final
        direction_to_check = righti
    elif (right in uc):
        vf = right
        final = final+vf
        direction_to_check = lefti

    next_to_space = grid.get(direction_to_check) == '.'
    
    if (vf is not None and next_to_space):
        return (True, final, direction_to_check)
    return (False,)

def is_outer(grid, p):
    return (p[0] <= grid.min_width+5 or 
            p[0] >= grid.width-5 or
            p[1] <= grid.min_height+5 or
            p[1] >= grid.height-5)

uc = set(string.ascii_uppercase)

f = open('input.txt')
grid = Grid()
for y,line in enumerate(f):
    line = line.rstrip()
    for x,c in enumerate(line):
        grid.put((x,y),c)

teleporters = defaultdict(list)
def check(p):
    v = is_teleporter_entrance(p)
    if (v[0]):
        teleporters[v[1]].append(v[2])
grid.iterate(check)
print(teleporters)

#for y in teleporters:
#    x = teleporters[y]
#    for c in x:
#        grid.put(c,'e')
#    print(y, x)
#grid.draw()

graph = defaultdict(list)
start = teleporters['AA'][0]
end = teleporters['ZZ'][0]
flood(start, 'AA')

for y in graph:
    x = graph[y]
    print(y, x)
bfs('AAOuter', 'ZZOuter')
