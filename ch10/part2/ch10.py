import sys
import math
import time

f = open(sys.argv[1])
asteroids_map = [l.strip() for l in f.readlines()]
width = len(asteroids_map[0])
height = len(asteroids_map)

asteroids = [(x,y) for y,l in enumerate(asteroids_map) for x,c in enumerate(l) if c == '#']

sign = lambda x: (1, -1)[x < 0]
def sort_key(a,b):
    x1,y1 = a
    x2,y2 = b

    angle = math.atan2(y1-y2, x1-x2)
    angle = (math.degrees(angle) + 360-90) % 360

    distance = (x1-x2)**2 + (y1-y2)**2

    return (angle,distance)


counts = []
for i,asteroid in enumerate(asteroids):
    if (asteroid != (30,34)):
        continue

    #print("Processing",asteroid)

    count = 0
    angle_list = []
    other_asteroids = sorted(asteroids[:i]+asteroids[i+1:], key=lambda b: sort_key(asteroid,b))

    copy = asteroids_map[:]
    while other_asteroids:
        other_asteroid = other_asteroids.pop(0)
        angle_list.append([other_asteroid])

        #print(sort_key(asteroid,other_asteroid))

        count += 1

        #print("At",other_asteroid)

        x,y = other_asteroid
        offset_x,offset_y = (other_asteroid[0]-asteroid[0], other_asteroid[1]-asteroid[1])
        if (asteroid[0] == x):
            offset_y = sign(offset_y)
        if (asteroid[1] == y):
            offset_x = sign(offset_x)
        if (abs(offset_x) == abs(offset_y)):
            offset_x = sign(offset_x)
            offset_y = sign(offset_y)
        offset_gcd = math.gcd(offset_x, offset_y)
        offset_x //= offset_gcd
        offset_y //= offset_gcd

        #copy[y] = copy[y][:x]+'.'+copy[y][x+1:]
        #time.sleep(0.05)
        #print(chr(27)+'[2j')
        #print('\033c')
        #print('\x1bc')
        #for line in copy:
        #    print(line)

        #print(x,y)
        #print(width,height)
        while (x>=0 and x<width) and (y>=0 and y<height):
            x += offset_x
            y += offset_y
            if ((x,y) in other_asteroids):
                #print("Deleting at", x,y)

                #copy[y] = copy[y][:x]+'.'+copy[y][x+1:]
                #time.sleep(0.05)
                #print(chr(27)+'[2j')
                #print('\033c')
                #print('\x1bc')
                #for line in copy:
                #    print(line)

                other_asteroids.remove((x,y))
                angle_list[-1].append((x,y))
        #print(other_asteroids)

    counts.append(count)

for i in range(200):
    asteroids = angle_list.pop(0)
    asteroid = asteroids.pop(0)
    if (len(asteroids) > 0):
        angle_list.append(asteroids)
print(asteroid)
#i = counts.index(max(counts))
#print(asteroids[i])
