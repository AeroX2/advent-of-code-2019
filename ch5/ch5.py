import sys

def nop():
    pass

def add(a,b,c):
    code[c] = code[a]+code[b]

def mul(a,b,c):
    code[c] = code[a]*code[b]

def inp(a):
    code[a] = int(input())

def out(a):
    print(code[a])

def get_param(p):
    global pc
    pc += 1
    #print(p,pc)
    if p == 0:
        return code[pc]
    elif p == 1:
        return pc

pc = 0
f = open(sys.argv[1])

run =   [nop, add, mul, inp, out]
run_p = {0:0, 1:3, 2:3, 3:1, 4:1, 99:0}

code = list(map(int,f.readline().strip().split(',')))
while True:
    ins = str(code[pc]).zfill(5)
    opcode = int(ins[-2:])
    parameter_options = [int(p) == 1 for p in ins[:-2]][::-1]

    actual_params = [get_param(parameter_options[p]) for p in range(run_p[opcode])]
    #print(actual_params)

    if (opcode == 99):
        #print(code)
        break
    run[opcode](*actual_params)
    pc += 1
    
    
    

     



