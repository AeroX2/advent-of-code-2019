import re
import sys
import math
from collections import defaultdict

class Chemical:
    def __init__(self, v):
        amount,name = v
        self.name = name
        self.amount = int(amount)

    def __str__(self):
        return "%s(%d)" % (self.name,self.amount)

    def __repr__(self):
        return "%s(%d)" % (self.name,self.amount)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

total_needed = defaultdict(lambda: None)
def process(in_graph, out_graph, fuel_node):
    q = [(fuel_node,1)]
    while (len(q)):
        node,amount_needed = q.pop(0)
         

        for n2 in in_graph[node]:
            q.append(n2)

in_graph = defaultdict(list)
out_graph = defaultdict(list)

reactions = []
for line in open(sys.argv[1]):
    line = line.strip()
    line = line.split(' => ')

    in_chems = [Chemical(c.split(' ')) for c in line[0].split(', ')]
    out_chems = [Chemical(c.split(' ')) for c in line[1].split(', ')]

    for chem in out_chems:
        in_graph[chem].extend(in_chems)

    for chem in in_chems:
        out_graph[chem].extend(out_chems)

print(in_graph)
print(out_graph)
chem = Chemical(('1','FUEL'))
print(process(in_graph, out_graph, chem))
