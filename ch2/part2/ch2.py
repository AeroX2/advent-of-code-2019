import sys

def brute(v1,v2):
    pc = 0
    f = open(sys.argv[1])
    code = list(map(int,f.readline().strip().split(',')))

    code[1] = v1
    code[2] = v2

    while True:
        opcode = code[pc]

        if opcode == 1:
            #print("add")
            #print(a,b,c)
            pc += 1
            a = code[code[pc]]
            pc += 1
            b = code[code[pc]]
            pc += 1
            c = code[pc]
            pc += 1
            code[c] = a+b
        elif opcode == 2:
            #print("mul")
            #print(a,b,c)
            pc += 1
            a = code[code[pc]]
            pc += 1
            b = code[code[pc]]
            pc += 1
            c = code[pc]
            pc += 1
            code[c] = a*b
        elif opcode == 99:
            if (code[0] == 19690720):
                print("Hey lmao",v1,v2)
            break


for i in range(0,100):
    for ii in range(0,100):
        brute(i,ii)

