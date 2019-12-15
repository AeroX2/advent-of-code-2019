from program import Program
from queue import Queue
from collections import deque

iq = Queue()
oq = Queue()

p = Program([],iq,oq)
t = p.run_from_file('input.txt')

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

    def find_free_location(self, robot_pos, invalids):
        valids = []
        for height in range(self.min_height-1, self.height+1):
            for width in range(self.min_width-1, self.width+1):
                v = (width, height)
                vg = self.get(v)
                if (v == robot_pos):
                    continue
                elif (v in invalids):
                    continue
                elif (vg is None):
                    valids.append((width,height))
        #print(valids)
        if (len(valids) <= 0):
            return None
        return list(sorted(valids, key=lambda p: (abs(p[0]-robot_pos[0])+abs(p[1]-robot_pos[1])))).pop(0)

    def flood_fill(self, oxygen_generator):
        seen = set()
        max_depth = 0
        queue = deque([(oxygen_generator,0)])
        while len(queue):
            pos,depth = queue.popleft()
            max_depth = max(max_depth, depth)

            if (pos in seen):
                continue
            seen.add(pos)

            for direction in [(0,1),(0,-1),(-1,0),(1,0)]:
                new_pos = (pos[0]+direction[0], pos[1]+direction[1])
                if (grid.get(new_pos) == '#'):
                    continue
                if (grid.get(new_pos) == 'O'):
                    continue
                grid.put(new_pos, 'O')
                queue.append((new_pos,depth+1))
            #grid.draw((0,0))
        return depth

    def draw(self, robot_pos):
        print(chr(27)+'[2j')
        print('\033c')
        print('\x1bc')
        string = ''
        for height in range(self.min_height-1, self.height+1):
            for width in range(self.min_width-1, self.width+1):
                v = (width, height)
                vg = self.get(v)
                if (v == robot_pos):
                    string += 'D'
                elif (vg is not None):
                    string += vg
                else:
                    string += 'N'
            string += '\n'
        print(string)

def bfs(src, dest, grid, final=False):
    if (grid.get((dest[0], dest[1]-1)) == '#' and 
        grid.get((dest[0], dest[1]+1)) == '#' and 
        grid.get((dest[0]-1, dest[1])) == '#' and 
        grid.get((dest[0]+1, dest[1])) == '#'):
        return None

    seen = set()
    queue = deque([(src,[])])
    while len(queue):
        pos,path = queue.popleft()
        #if (len(path) > 500):
        #    break

        if (pos in seen):
            continue
        seen.add(pos)

        if (pos == dest):
            return path

        for direction in [(0,1),(0,-1),(-1,0),(1,0)]:
            new_pos = (pos[0]+direction[0], pos[1]+direction[1])
            if (grid.get(new_pos) == '#'):
                continue
            if (final and grid.get(new_pos) is None):
                continue
            queue.append((new_pos,path[:]+[new_pos]))
    return None

robot_pos = (0,0)
invalids = set()
grid = Grid()
while (t.is_alive() or not oq.empty()):
    free_location = grid.find_free_location(robot_pos, invalids)
    if (free_location is None):
        print("Minutes to fill", grid.flood_fill(oxygen_generator))
        import sys; sys.exit()
    grid.draw(robot_pos)
    #print("Next free location", free_location)
    #print("Robot position", robot_pos)
    path_to_free = bfs(robot_pos, free_location, grid)
    if (path_to_free is None):
        invalids.add(free_location)
        continue
    #print("Path to free", path_to_free)

    while (len(path_to_free)):
        next_pos = path_to_free.pop(0)
        direction = (next_pos[0]-robot_pos[0], next_pos[1]-robot_pos[1])
        if (direction[1] > 0):
            direction = 1
        elif (direction[1] < 0):
            direction = 2
        elif (direction[0] < 0):
            direction = 3
        elif (direction[0] > 0):
            direction = 4

        iq.put(direction)
        output = oq.get()
        grid.draw(robot_pos)

        if (output == 0):
            #print("Found wall at",next_pos)
            grid.put(next_pos, '#')
            break
        elif (output == 1):
            #print("Moving to",next_pos)
            grid.put(next_pos, ' ')
            robot_pos = next_pos
        elif (output == 2):

            grid.put(next_pos, 'O')
            path = bfs((0,0),next_pos,grid,True)
            print("Oxygen generator found at",next_pos)
            print("Length of path to oxygen", len(path))
            import time; time.sleep(5)

            oxygen_generator = next_pos
            robot_pos = next_pos
