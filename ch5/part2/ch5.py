import sys

def nop():
    pass

def add(a,b,c):
    code[c] = code[a]+code[b]

def mul(a,b,c):
    code[c] = code[a]*code[b]

def inp(a):
    code[a] = int(input("Input: "))

def out(a):
    print(code[a])

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
    if p == 0:
        return code[pc]
    elif p == 1:
        return pc

f = open(sys.argv[1])

run =   [nop, add, mul, inp, out, jt, jf, lt, eq]
run_p = {0:0, 1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 99:0}

for line in f:
    pc = 0
    code = list(map(int,line.strip().split(',')))
    while True:
        ins = str(code[pc]).zfill(5)
        opcode = int(ins[-2:])
        parameter_options = [int(p) == 1 for p in ins[:-2]][::-1]

        #print(opcode)
        actual_params = [get_param(parameter_options[p]) for p in range(run_p[opcode])]
        #print(actual_params)

        if (opcode == 99):
            #print(code)
            break

        run[opcode](*actual_params)
        pc += 1
    
    
    

     



