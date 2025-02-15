from program import Program
from queue import Queue
from collections import defaultdict

computers = []
for i in range(50):
    iq = Queue()
    iq.put(i)
    oq = Queue()
    p = Program([],iq,oq)
    t = p.run_from_file('input.txt')
    computers.append((iq,oq,p))

packets = defaultdict(list)
while True:
    for i,computer in enumerate(computers):
        iq = computer[0]
        oq = computer[1]
        p = computer[2]

        if (len(packets[i]) > 0):
            for packet in packets[i]:
                iq.put(packet[0])
                iq.put(packet[1])
            packets[i] = []
        else:
            iq.put(-1)

        while (not oq.empty()):
            address = oq.get()
            x = oq.get()
            y = oq.get()

            if (address == 255):
                print(x,y)
                import sys; sys.exit()
            else:
                packets[address].append((x,y))
