from program import Program
from queue import Queue
from collections import deque

iq = Queue()
oq = Queue()

p = Program([],iq,oq)
t = p.run_from_file('input.txt')
#p.code[0] = 2
t.start()

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

    def intersections(self, robot_pos):
        commands = []
        points = set()

        def test_direction(robot_pos, d):
            if (d == 0):   p = (robot_pos[0], robot_pos[1]-1)
            elif (d == 1): p = (robot_pos[0]+1, robot_pos[1])
            elif (d == 2): p = (robot_pos[0], robot_pos[1]+1)
            elif (d == 3): p = (robot_pos[0]-1, robot_pos[1])

            v = self.get(p)
            return (v == '#', p)

        direction = 0
        while True:
            # Keep going forward until empty
            length = 0
            while True:
                v = test_direction(robot_pos, direction)
                if (not v[0]):
                    break
                #grid.put(robot_pos, '#')
                robot_pos = v[1]
                #grid.put(robot_pos, '^')
                #import time; time.sleep(0.5)
                #grid.draw()
                length += 1

            # Test left and right
            if (test_direction(robot_pos, (direction-1)%4)[0]):
                direction = (direction-1)%4
                commands.append(str(length))
                commands.append("L")
                #print("Length", length, "Going left")
            elif (test_direction(robot_pos, (direction+1)%4)[0]):
                direction = (direction+1)%4
                commands.append(str(length))
                commands.append("R")
                #print("Length", length, "Going right")
            else:
                commands.append(str(length))
                break

        return commands

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

grid = Grid()
x,y = (0,0)
while (t.is_alive() or not oq.empty()):
    o = oq.get()
    if (o == 10):
        x = 0
        y += 1
        continue
    if (o == ord('^')):
        robot_pos = (x,y)
    grid.put((x,y), chr(o))
    x += 1

commands = grid.intersections(robot_pos)
commands.pop(0)
print(','.join(commands))

q = [(commands,[])]
while (len(q)):
    c,l = q.pop(0)

    if (len(l) > 3):
        continue

    if (len([x for x in c if x != ' ']) <= 0 and len(l) == 3):
        break

    #c = [x if x != '' else 'X' for x in c]
    for s,x in enumerate(c):
        if (x != ' '):
            break

    for g in range(s+1,len(c)):
        if (c[g] == ' '):
            break

        new_ss = c[s:g+1]
        new_c = c[:]

        for i in range(len(new_c)):
            if new_c[i:i+len(new_ss)] == new_ss:
                #del new_c[i:i+len(new_ss)]
                for ii in range(i,i+len(new_ss)):
                    new_c[ii] = ' '

        new_l = l[:]
        new_l.append(new_ss)
        
        q.append((new_c, new_l))
else:
    print("Failed")

print(l)
print([','.join(c) for c in l])

indexes = []
for i,x in enumerate(l):
    print(x)
    for ii in range(len(commands)):
        if commands[ii:ii+len(x)] == x:
            indexes.append((ii,i)) 
print(sorted(indexes))

iq = Queue()
p = Program([],iq,oq)
t = p.run_from_file('input.txt')
p.code[0] = 2
t.start()

for i,z in enumerate(sorted(indexes)):
    if (z[1] == 0):
        iq.put(ord('A'))
    elif (z[1] == 1):
        iq.put(ord('B'))
    elif (z[1] == 2):
        iq.put(ord('C'))

    if (i < len(indexes)-1):
        iq.put(ord(','))
iq.put(ord('\n'))

for c in l:
    print(c)
    for z in ','.join(c):
        iq.put(ord(z))
    iq.put(ord('\n'))
iq.put(ord('n'))
iq.put(ord('\n'))

x = 0
y = 0
while (t.is_alive() or not oq.empty()):
    o = oq.get()
    print(o)
