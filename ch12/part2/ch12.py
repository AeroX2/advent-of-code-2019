import re
import math
cmp = lambda a,b: (a>b)-(a<b)

class Planet:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

        self.vx = 0
        self.vy = 0
        self.vz = 0

    def update_vel(self, others):
        for other_p in others:
            #self.vx += cmp(self.x, other_p.x)
            self.vx += cmp(other_p.x, self.x)
            self.vy += cmp(other_p.y, self.y)
            self.vz += cmp(other_p.z, self.z)

    def update_pos(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

planets = []
for line in open('input.txt'):
    m = re.match(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>', line.strip()) 

    x = int(m.group(1))
    y = int(m.group(2))
    z = int(m.group(3))

    planets.append(Planet(x,y,z))

steps = 0

i_x_pos = tuple([(p.x,p.vx) for p in planets])
i_y_pos = tuple([(p.y,p.vy) for p in planets])
i_z_pos = tuple([(p.z,p.vz) for p in planets])

x_rep = None
y_rep = None
z_rep = None

while True:

    for i,p in enumerate(planets):
        p.update_vel(planets[:i]+planets[i+1:])
    for p in planets:
        p.update_pos()
    steps += 1

    x_pos = tuple([(p.x,p.vx) for p in planets])
    if (x_pos == i_x_pos and x_rep is None):
        x_rep = steps
    y_pos = tuple([(p.y,p.vy) for p in planets])
    if (y_pos == i_y_pos and y_rep is None):
        y_rep = steps
    z_pos = tuple([(p.z,p.vz) for p in planets])
    if (z_pos == i_z_pos and z_rep is None):
        z_rep = steps

    if (x_rep is not None and
        y_rep is not None and
        z_rep is not None):
        print(x_rep,y_rep,z_rep)
        q = (x_rep*y_rep) // math.gcd(x_rep, y_rep)
        q = (q*z_rep) // math.gcd(q, z_rep)
        print(q)
        break
