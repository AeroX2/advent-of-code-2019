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

nat = None
last_nat = (0,0)

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
                nat = (x,y)
            else:
                packets[address].append((x,y))

    if (all([len(p) <= 0 for p in packets.values()]) and
        all([c[0].empty() for c in computers]) and
        all([c[1].empty() for c in computers]) and
            nat):
        wait = True
        print("Delivering NAT", nat)
        packets[0] = [nat]
        if (nat == last_nat):
            print("Same NAT", nat)
            import sys; sys.exit()
        last_nat = nat

#while (t.is_alive() or not oq.empty()):
#    o = oq.get()
#    if (o == 10):
#        x = 0
#        y += 1
#        continue
#    if (o == ord('^')):
#        robot_pos = (x,y)
#    grid.put((x,y), chr(o))
#    x += 1

