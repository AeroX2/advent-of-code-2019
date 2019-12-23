stack = [i for i in range(10007)]

f = open('input.txt')
for read in f.readlines():
    print("Result:", stack[:10])
    if ("deal into new stack" in read):
        stack = stack[::-1]
    elif ("cut" in read):
        offset = int(read[3:])
        stack = stack[offset:]+stack[:offset]
    elif ("deal with increment" in read):
        offset = int(read[19:])

        new_stack = [0]*len(stack)
        for i,v in enumerate(stack):
            new_stack[(i*offset)%len(new_stack)] = stack[i]
        stack = new_stack
print("Final Result:", stack[:10])
print("Index 2019:", stack.index(2019))

