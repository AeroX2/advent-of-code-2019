class Planet:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        print("INIT",x,y,z)

        self.vx = 0
        self.vy = 0
        self.vz = 0

    def update_vel(self, others):
        for other_p in others:
            #self.vx += cmp(self.x, other_p.x)
            self.vx += cmp(other_p.x, self.x)
            self.vy += cmp(other_p.y, self.y)
            self.vz += cmp(other_p.z, self.z)
        print(self.vx, self.vy, self.vz)

    def update_pos(self):
        print(self.x, self.y, self.z)
        print(self.vx, self.vy, self.vz)
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        print("U",self.x, self.y, self.z)


import re
cmp = lambda a,b: (a>b)-(a<b)

planets = []
for line in open('input.txt'):
    m = re.match(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', line.strip()) 

    x = int(m.group(1))
    y = int(m.group(2))
    z = int(m.group(3))

    planets.append(Planet(x,y,z))

for i in range(1000):
    for i,p in enumerate(planets):
        p.update_vel(planets[:i]+planets[i+1:])
    for p in planets:
        p.update_pos()

total = 0
for p in planets:
    total += (abs(p.x)+abs(p.y)+abs(p.z)) * (abs(p.vx)+abs(p.vy)+abs(p.vz))
print(total)

    
