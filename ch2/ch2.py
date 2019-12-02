import sys

pc = 0
f = open(sys.argv[1])
code = list(map(int,f.readline().strip().split(',')))
while True:
    opcode = code[pc]

    if opcode == 1:
        print("add")
        pc += 1
        a = code[code[pc]]
        pc += 1
        b = code[code[pc]]
        pc += 1
        c = code[pc]
        pc += 1
        code[c] = a+b
        print(a,b,c)
    elif opcode == 2:
        print("mul")
        print(a,b,c)
        pc += 1
        a = code[code[pc]]
        pc += 1
        b = code[code[pc]]
        pc += 1
        c = code[pc]
        pc += 1
        code[c] = a*b
    elif opcode == 99:
        print(code[0])
        break
    print(code)

