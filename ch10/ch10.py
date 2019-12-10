import sys
import math
import time

f = open(sys.argv[1])
asteroids_map = [l.strip() for l in f.readlines()]
width = len(asteroids_map[0])
height = len(asteroids_map)

asteroids = [(x,y) for y,l in enumerate(asteroids_map) for x,c in enumerate(l) if c == '#']
sign = lambda x: (1, -1)[x < 0]


counts = []
for i,asteroid in enumerate(asteroids):
#for i,asteroid in enumerate(asteroids):
    #if (asteroid != (11,13)):
    #    continue

    #print("Processing",asteroid)

    count = 0
    other_asteroids = sorted(asteroids[:i]+asteroids[i+1:], key=lambda x: (asteroid[0]-x[0])**2+(asteroid[1]-x[1])**2)

    #copy = asteroids_map[:]

    while other_asteroids:
        other_asteroid = other_asteroids.pop(0)
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
        #print(other_asteroids)

    counts.append(count)
print(max(counts))
print(dict(zip(asteroids,counts)))

        

