stack_size = 119315717514047
stack_size = 10007

n = 2020
n = 2019

index = n

f = open('input.txt')
arr = f.readlines()
for i,read in enumerate(arr[::-1]):
    if ("deal into new stack" in read):
        n = stack_size - n - 1
    elif ("cut" in read): # cut
        offset = int(read[3:])
        n += offset
        n %= stack_size
    elif ("deal with increment" in read):
        offset = int(read[19:])
        # TODO MATHS

print("Estimated Number at %d:" % index, n)

stack = [i for i in range(stack_size)]

f = open('input.txt')
for read in f.readlines():
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
print("Number at %d:" % index, stack[index])

