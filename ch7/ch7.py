import sys
from itertools import permutations

def nop():
    pass

def add(a,b,c):
    code[c] = code[a]+code[b]

def mul(a,b,c):
    code[c] = code[a]*code[b]

def inp(a):
    code[a] = int(inp_p.pop())

def out(a):
    out_p.append(code[a])

def jt(a,b):
    global pc
    if (code[a] != 0):
        pc = code[b]-1

def jf(a,b):
    global pc
    if (code[a] == 0):
        pc = code[b]-1

def lt(a,b,c):
    code[c] = code[a] < code[b]

def eq(a,b,c):
    code[c] = code[a] == code[b]


def get_param(p):
    global pc
    pc += 1
    #print(p,pc)
    if (p == 0):
        return code[pc]
    elif (p == 1):
        return pc

f = open(sys.argv[1])
code = list(map(int,f.readline().strip().split(',')))

run =   [nop, add, mul, inp, out, jt, jf, lt, eq]
run_p = {0:0, 1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 99:0}

final = 0
for inputs in permutations([0,1,2,3,4]):
    inputs = list(inputs)

    inp_p = []
    out_p = []
    while inputs:
        inp_p.append(out_p.pop() if len(out_p) else 0)
        inp_p.append(inputs.pop())

        pc = 0
        while True:
            ins = str(code[pc]).zfill(5)
            opcode = int(ins[-2:])
            parameter_options = [int(p) == 1 for p in ins[:-2]][::-1]

            actual_params = [get_param(parameter_options[p]) for p in range(run_p[opcode])]
            #print(actual_params)

            if (opcode == 99):
                break

            run[opcode](*actual_params)
            pc += 1

    final = max(final,out_p[0])
print(final)

