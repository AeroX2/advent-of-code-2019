from shapely.geometry import LineString, Point

f = open('input.txt')

lines = []
for line in f:
    line = line.split(',')
    coords = [(0,0)]
    for i,v in enumerate(line):
        p = coords[-1]
        d = v[0]
        vl = int(v[1:])
        if d == 'U':
            coords.append((p[0],p[1]+vl))
        elif d == 'D':
            coords.append((p[0],p[1]-vl))
        elif d == 'L':
            coords.append((p[0]-vl,p[1]))
        elif d == 'R':
            coords.append((p[0]+vl,p[1]))
    lines.append(LineString(coords))

def line_distance(line, intersection):
    calculated = 0
    for i in range(len(line.coords)-1):
        pcoord = Point(line.coords[i])
        coord = Point(line.coords[i+1])

        #print(pcoord, coord)

        minx = min(pcoord.x, coord.x)
        maxx = max(pcoord.x, coord.x)

        miny = min(pcoord.y, coord.y)
        maxy = max(pcoord.y, coord.y)

        if ((coord.x == intersection.x and (intersection.y > miny and intersection.y < maxy)) or
            (coord.y == intersection.y and (intersection.x > minx and intersection.x < maxx))):
            calculated += abs(pcoord.x-intersection.x)+abs(pcoord.y-intersection.y)
            break
        calculated += abs(pcoord.x-coord.x)+abs(pcoord.y-coord.y)
    return calculated

closest = 10000000
for i,line in enumerate(lines):
    for other_line in lines[i+1:]:
        for intersection in (line.intersection(other_line)):
            if (intersection.x == 0 and intersection.y == 0):
                continue
            
            calculated = line_distance(line, intersection) + line_distance(other_line, intersection)
            closest = min(closest, calculated)
            
print(closest)

