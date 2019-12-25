class Grid:
    def __init__(self):
        self.grid = {}
        self.width = 1
        self.height = 1
        self.min_width = 0
        self.min_height = 0

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
        for y in range(self.min_height, self.height+1):
            for x in range(self.min_width, self.width+1):
                fn((x,y))

    def draw(self):
        #print(chr(27)+'[2j')
        #print('\033c')
        #print('\x1bc')
        string = ''
        for y in range(self.min_height, self.height+1):
            for x in range(self.min_width, self.width+1):
                v = (x, y)
                vg = self.get(v)
                if (vg != ''):
                    string += vg
            string += '\n'
        print(string)

grid = Grid()
for y,line in enumerate(open('input.txt')):
    line = line.strip()
    for x,c in enumerate(line):
        grid.put((x,y),c)

new_grid = Grid()
def update(p):
    up    = grid.get((p[0], p[1]-1))
    down  = grid.get((p[0], p[1]+1))
    left  = grid.get((p[0]-1, p[1]))
    right = grid.get((p[0]+1, p[1]))
    count = sum([up == '#',
                 down == '#',
                 left == '#',
                 right == '#'])

    if (grid.get(p) == '#'):
        if (count != 1):
            new_grid.put(p, '.')
        else:
            new_grid.put(p, '#')
    elif (grid.get(p) == '.'):
        if (count == 1 or
            count == 2):
            new_grid.put(p, '#')
        else:
            new_grid.put(p, '.')

total = 0
def calc(p):
    global total
    if (grid.get(p) == '#'):
        v = p[1]*(grid.width+1) + p[0]
        q = 2**v
        total += q

unique = set()
while True:
    grid.draw()
    new_grid = Grid()
    grid.iterate(update)
    new_grid.draw()
    grid = new_grid
    total = 0
    grid.iterate(calc)
    if (total in unique):
        grid.draw()
        print(total)
        import sys; sys.exit()
    unique.add(total)
    print(total)

