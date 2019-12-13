from program import Program
from queue import Queue

iq = Queue()
oq = Queue()

p = Program([],iq,oq)
t = p.run_from_file('input.txt')

count = 0
while (t.is_alive() or not oq.empty()):
    x = oq.get()
    y = oq.get()
    tid = oq.get()
    print((x,y,tid))
    if (tid == 2):
        count += 1
print(count)
