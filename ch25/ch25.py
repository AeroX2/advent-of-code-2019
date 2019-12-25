from program import Program
from queue import Queue
from collections import defaultdict

iq = Queue()
oq = Queue()
p = Program([],iq,oq)
t = p.run_from_file('input.txt')

def inp(iq,s):
    for c in s:
        iq.put(ord(c))
    iq.put(ord('\n'))

inp(iq,"north")
inp(iq,"take mutex")
inp(iq,"south")
inp(iq,"west")
inp(iq,"take space law space brochure")
inp(iq,"north")
inp(iq,"take loom")
inp(iq,"south")
inp(iq,"south")
inp(iq,"take hologram")
inp(iq,"west")
inp(iq,"take manifold")
inp(iq,"east")
inp(iq,"north")
inp(iq,"east")
inp(iq,"south")
inp(iq,"take cake")
inp(iq,"west")
inp(iq,"south")
inp(iq,"take easter egg")
inp(iq,"south")
inp(iq,"south")

items = ["mutex", "space law space brochure", "loom", "hologram", "manifold", "cake", "easter egg"]
for item in items:
    inp(iq,"drop %s" % item)

from itertools import combinations
for i in range(1,len(item)+1):
    for combination in combinations(items, i):
        for item in combination:
            inp(iq, "take %s" % item)
        inp(iq, "south")
        for item in combination:
            inp(iq, "drop %s" % item)

full_string = ''
last_index = 0
while True:
    string = ''
    while (not oq.empty()):
        c = oq.get()
        string += chr(c)

    full_string += string
    if (string.replace('\n','')):
        print(string,end='')

    if (iq.empty() and "Command?" in full_string[last_index+1:]):
        last_index += full_string[last_index+1:].index("Command?")
        s = input()
        if (s):
            for c in s:
                iq.put(ord(c))
            iq.put(ord('\n'))
        import time; time.sleep(0.1)

