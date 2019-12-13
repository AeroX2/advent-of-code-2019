from program import Program
from queue import Queue

iq = Queue()
oq = Queue()
dq = Queue()

p = Program([],iq,oq,dq)
t = p.run_from_file('input.txt')
p.code[0] = 2
t.start()

class Grid:
    def __init__(self):
        self.grid = {}
        self.width = 0
        self.height = 0

    def put(self, pos, item):
        self.width = max(self.width, pos[0])
        self.height = max(self.height, pos[1])
        self.grid[pos] = item

    def get(self, pos):
        return self.grid[pos]

    def draw(self):
        for height in range(self.height+1):
            for width in range(self.width+1):
                if ((width,height) in self.grid):
                    if (self.grid[(width,height)] == 0):
                        print(' ',end='')
                    else:
                        print(self.grid[(width,height)], end='')
                else:
                    print(' ',end='')
            print()

dq.put(0)

score = 0
grid = Grid()
while (t.is_alive() or not oq.empty()):
    #c = getch.getch()
    #time.sleep(0.01)
    #c = input()
    #if (c == 'h'):
    #    iq.put(-1)
    #elif (c == 'l'):
    #    iq.put(1)
    #else:
    iq.put(0)

    while (not oq.empty()):
        x = oq.get()[1]
        y = oq.get()[1]
        q,tid = oq.get()

        if (x == -1 and y == 0):
            print(q)
            score = tid
        else:
            grid.put((x,y),tid)

    #print(chr(27)+'[2j')
    #print('\033c')
    #print('\x1bc')
    #print(score)
    #grid.draw()

print(score)
