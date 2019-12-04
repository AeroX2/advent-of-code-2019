low = 109165
high = 576723 

def recurse(base, end, depth=0):
    if (int(base) >= end):
        return 0

    if (depth == 6):
        count = 0
        prev = None
        for i,v in enumerate(base[:-1]):
            if (base[i] == base[i+1]):
                return 1
        return 0


    count = 0
    a = int(base[depth-1]) if depth > 0 else int(base[depth])
    #print(a)
    for i in range(a,10):
        copy = base[:depth]+str(i)+base[depth+1:]
        count += recurse(copy, end, depth+1)
    return count

print(recurse(str(low), high))

