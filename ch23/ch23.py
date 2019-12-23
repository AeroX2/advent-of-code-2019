from program import Program
from queue import Queue
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

    def draw(self):
        #print(chr(27)+'[2j')
        #print('\033c')
        #print('\x1bc')
        string = ''
        for height in range(self.min_height-1, self.height+1):
            for width in range(self.min_width-1, self.width+1):
                v = (width, height)
                vg = self.get(v)
                if (vg is not None):
                    string += vg
            string += '\n'
        print(string)

count = 0
grid = Grid()
for x in range(0,50):
    for y in range(0,50):
        iq = Queue()
        oq = Queue()
        p = Program([],iq,oq)
        t = p.run_from_file('input.txt')
        #t.start()
        iq.put(x)
        iq.put(y)
        v = oq.get()
        if (v == 1):
            count += 1
        grid.put((x,y), str(v))
print(count)
        


#while (t.is_alive() or not oq.empty()):
#    o = oq.get()
#    if (o == 10):
#        x = 0
#        y += 1
#        continue
#    if (o == ord('^')):
#        robot_pos = (x,y)
#    grid.put((x,y), chr(o))
#    x += 1

