import re
import sys
import math

reactions = []
for line in open(sys.argv[1]):
    line = line.strip()
    line = line.split(' => ')

    reactants = {}
    for l in line[0].split(', '):
        a,b = l.split()
        reactants[b] = int(a)

    products = {}
    for l in line[1].split(', '):
        a,b = l.split()
        products[b] = int(a)

    reactions.append((reactants,products))

def find_reactions_for_reactants(reactant):
    return [r for r in reactions if product in r[0]]

def find_reactions_for_product(product):
    return [r for r in reactions if product in r[1]]

#def recurse(output, amount, path=[]):
#    print(output, amount)
#    if (output == 'ORE'):
#        print('Found path', path)
#        return (True,[])
#
#    valid_reactions = []
#    all_reactions = find_reactions_for_product(output)
#    for reaction in all_reactions:
#        # Find all needed items  
#        print("R", reaction)
#        for reactant,q in reaction[0].items():
#            print("Rea", reactant)
#            valid_path,leftovers = recurse(reactant, q)
#            if (not valid_path):
#                print("WAT")
#                break
#        else:
#            valid_reactions.append(reaction)
#    print("V", valid_reactions)
#
#    return (len(valid_reactions) <= 0, [])

def recurse(needed, amount_needed):
    pass

#
#
#print(recurse('FUEL',1,[]))
#print(brute_force('FUEL',1,[]))
