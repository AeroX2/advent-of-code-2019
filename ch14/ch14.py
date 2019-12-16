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

resolved = set(['FUEL'])
total_needed = defaultdict(lambda: 0)
def process(in_graph, out_graph, fuel_node):

    total = 0
    total_needed['FUEL'] = 1
    q = [fuel_node]
    while (len(q)):
        node = q.pop(0)
        resolved.add(node.name)
        print(resolved)
        print(total_needed)
        print(node,end= ' ')

        for chem_out in out_graph[node]:
            #Check if calculated
            if (chem_out.name not in resolved):
                print("ignore")
                q.append(node)
                break
        else:
            print("continue")

            if ('ORE' in node.name):
                ore_needed = node.amount
                for chem_out in out_graph[node]:
                    amount_needed = total_needed[chem_out.name]
                    amount_produced = chem_out.amount

                    v = math.ceil(amount_needed / amount_produced) * ore_needed
                    total += v
                print("T",total)

            for chem_in in in_graph[node]:
                amount_needed = total_needed[node.name]
                amount_produced = [c for c in in_graph if c == node][0].amount #node.amount

                print("B",amount_needed, amount_produced, chem_in, node)

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

print(in_graph)
print(out_graph)
chem = Chemical(('1','FUEL'))
print(process(in_graph, out_graph, chem))

