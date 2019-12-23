stack = [i for i in range(10007)]

f = open('input.txt')
arr = f.readlines()*1000
for i,read in enumerate(arr):
    #print("Result:", stack[:10])
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
