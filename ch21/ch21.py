from program import Program
from queue import Queue

iq = Queue()
oq = Queue()
p = Program([],iq,oq)
t = p.run_from_file('input.txt')

def add_input(q, l):
    for c in l:
        q.put(ord(c))
    q.put(ord('\n'))

# pos = 0
# if (no ground at A and ground at D) = if (not A and D)
# if (no ground at C and ground at D) = if (not C and D)

add_input(iq, "NOT A T")  
add_input(iq, "AND D T")  
add_input(iq, "OR T J")  

add_input(iq, "NOT C T")  
add_input(iq, "AND D T")  
add_input(iq, "OR T J")  

add_input(iq, "WALK") 

while (t.is_alive() or not oq.empty()):
    o = oq.get()
    print(o)

