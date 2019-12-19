from program import Program
from queue import Queue
from collections import deque

class Grid:
    def __init__(self):
        self.grid = {}
        self.width = 1
        self.height = 1
        self.min_width = None
        self.min_height = None

    def put(self, pos, item):
        self.width = max(self.width, pos[0])
        self.height = max(self.height, pos[1])

        if (self.min_width is None):
            self.min_width = pos[0]
        self.min_width = min(self.min_width, pos[0])
        if (self.min_height is None):
            self.min_height = pos[1]
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

#from math import *
#min_x = 100000000
#min_y = 100000000
#max_x = 0
#max_y = 0
#def calc(p1,p2):
#    global min_x
#    global min_y
#    global max_x
#    global max_y
#
#    if (p1 == p2):
#        return
#
#    a1 = atan2(p2[1],p2[0])
#    a2 = atan2(p1[1],p1[0])
#    a3 = a2 - a1
#
#    x = 100 * tan(radians(90)-a3)
#    d = 100 + x
#
#    ud = d / sin(a3) * sin(a1)
#
#    x = sin(radians(90)-a3) * ud
#    y = cos(radians(90)-a3) * ud
#    print(x,y)
#
#    x = int(x)
#    y = int(y)
#    min_x = min(min_x, x)
#    min_y = min(min_y, y)
#    max_x = max(max_x, x)
#    max_y = max(max_y, y)
#    print(degrees(a1),degrees(a2),degrees(a3))

from math import *
def calc(p1,p2):
    k2 = p1[1]/p1[0]
    k1 = p2[1]/p2[0]

    d = 100
    x = (-d - d/2*(k1+k2)) / (k1-k2)
    y = k1*(x + d/2) + d/2
    yz = k2*(x - d/2) - d/2

    x2 = int(x) - d//2
    y2 = int(y) - d//2
    print(x2,y2)
    for i in range(-100,100):
        for ii in range(-100,100):
            x = x2 + i
            y = y2 + ii

            # Test point
            iq.put(x)
            iq.put(y)
            p = Program(code,iq,oq)
            p.run()
            p1 = oq.get()

            iq.put(x+99)
            iq.put(y)
            p = Program(code,iq,oq)
            p.run()
            p2 = oq.get()

            iq.put(x)
            iq.put(y+99)
            p = Program(code,iq,oq)
            p.run()
            p3 = oq.get()

            iq.put(x+100)
            iq.put(y)
            p = Program(code,iq,oq)
            p.run()
            p4 = oq.get()

            iq.put(x)
            iq.put(y+100)
            p = Program(code,iq,oq)
            p.run()
            p5 = oq.get()

            if (p1 == 1 and p2 == 1 and p3 == 1 and p4 == 0 and p5 == 0):
                print("Found valid at", (x,y))


code = list(map(int,open('input.txt').readline().strip().split(',')))+[0]*10000
iq = Queue()
oq = Queue()

count = 0
grid = Grid()
a = 1000
for y in range(a,a+1000):
    found = None
    for x in range(0,10000000000000000):
        iq.put(x)
        iq.put(y)
        p = Program(code,iq,oq)
        p.run()
        #t.start()
        #print("wat")
        v = oq.get()
        #print(v)
        if (found is None and v == 1):
            found = (x,y)
        if (found is not None and v == 0):
            print(found,(x-1,y))
            calc(found,(x-1,y))
            break

#print(min_x, max_x, min_y, max_y)
#for y in range(21000,21000+1000):
#    found = None
#    for x in range(0,100000000000000000):
#        iq.put(x)
#        iq.put(y)
#        p = Program(code,iq,oq)
#        p.run()
#
#        v = oq.get()
#        if (found is None and v == 1):
#            found = (x,y)
#        if (found is not None and v == 0):
#            print(found)
#            print(x,y)
#            import sys; sys.exit()
#            break
#        #grid.put((x,y), str(v))
#    #grid.draw()

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

