import math

def calc(v):
    final = 0;
    while v > 0:
        v = math.floor(v/3)-2
        if (v > 0):
            final += v
    return final

output = 0
for l in open('input.txt'):
    output += calc(int(l))
print(output)
