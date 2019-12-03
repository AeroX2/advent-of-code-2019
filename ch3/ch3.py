from shapely.geometry import LineString

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

closest = None
for i,line in enumerate(lines):
    for other_line in lines[i+1:]:
        for intersection in (line.intersection(other_line)):
            if (intersection.x == 0 and intersection.y == 0):
                continue
            
            if closest is None:
                closest = intersection
            elif (abs(intersection.x)+abs(intersection.y) < abs(closest.x)+abs(closest.y)):
                closest = intersection
print(closest)

