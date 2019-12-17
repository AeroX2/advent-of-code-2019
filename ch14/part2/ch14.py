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

def process(in_graph, out_graph, fuel_node):
    total = 0
    resolved = set()
    total_needed = defaultdict(lambda: 0)
    total_needed['FUEL'] = fuel_node.amount
    q = [fuel_node]
    while (len(q)):
        node = q.pop(0)
        #print(resolved)
        #print(total_needed)
        #print(node,end= ' ')

        for chem_out in out_graph[node]:
            #Check if calculated
            if (chem_out.name not in resolved):
                #print("ignore")
                q.append(node)
                break
        else:
            #print("continue")
            resolved.add(node.name)

            if ('ORE' in node.name):
                ore_needed = node.amount
                for chem_out in out_graph[node]:
                    amount_needed = total_needed[chem_out.name]
                    amount_produced = chem_out.amount

                    v = math.ceil(amount_needed / amount_produced) * ore_needed
                    total += v
                #print("T",total)

            for chem_in in in_graph[node]:
                amount_needed = total_needed[node.name]
                amount_produced = [c for c in in_graph if c == node][0].amount #node.amount

                #print("B",amount_needed, amount_produced, chem_in, node)

                v = math.ceil(amount_needed / amount_produced) * chem_in.amount
                total_needed[chem_in.name] += v
                if not chem_in in q:
                    q.append(chem_in)
    return total

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
        if (chem.name == 'ORE'):
            chem.name += str(chem.amount)

        out_graph[chem].extend(out_chems)

def binary_search(in_graph, out_graph, low, high):
    while low <= high:
        mid = (low + high) // 2
        chem = Chemical((str(mid),'FUEL'))
        v = process(in_graph, out_graph, chem)
        if (v > 1000000000000):
            high = mid-1
        elif (v < 1000000000000):
            low = mid+1
    print(low,high)

chem = Chemical((str(460664),'FUEL'))
v = process(in_graph, out_graph, chem)
print("VVVVV",v)

pm = 0
m = 1
while True:
    chem = Chemical((str(m),'FUEL'))
    ore = process(in_graph, out_graph, chem)
    if (ore < 1000000000000):
        pm = m
        m *= 2
    elif (ore > 1000000000000):
        print("Stage 2")
        print("Low",pm,"High",m)
        low = pm
        high = m
        binary_search(in_graph, out_graph, low, high)
        break

