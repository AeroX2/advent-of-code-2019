import sys
#from queue import Queue
from threading import Thread
from multiprocessing import Process, Queue
from itertools import permutations

class Program:
    def __init__(self,
                 code,
                 input_stream,
                 output_stream,
                 final_stream=None,
                 name=''):
        self.ops           = [self.nop, self.add, self.mul, self.inp, self.out, self.jt, self.jf, self.lt, self.eq]
        self.op_parameters = {0:0, 1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 99:0}

        #self.stop = False
        self.last_output = None

        self.code = code[:]
        self.input_stream = input_stream
        self.output_stream = output_stream

        self.final_stream = final_stream
        self.name = name

    def nop(self):
        pass

    def add(self,a,b,c):
        self.code[c] = self.code[a]+self.code[b]

    def mul(self,a,b,c):
        self.code[c] = self.code[a]*self.code[b]

    def inp(self,a):
        #code[a] = int(inp_p.pop())
        v = self.input_stream.get()
        #if (v is None):
        #    self.stop = True
        #print("Input for program",self.name,v)
        self.code[a] = v 

    def out(self,a):
        #self.out_p.append(code[a])
        self.last_output = self.code[a]
        self.output_stream.put(self.code[a])

    def jt(self,a,b):
        if (self.code[a] != 0):
            self.pc = self.code[b]-1

    def jf(self,a,b):
        if (self.code[a] == 0):
            self.pc = self.code[b]-1

    def lt(self,a,b,c):
        self.code[c] = self.code[a] < self.code[b]

    def eq(self,a,b,c):
        self.code[c] = self.code[a] == self.code[b]


    def get_param(self,p):
        self.pc += 1
        #print(p,pc)
        if (p == 0):
            return self.code[self.pc]
        elif (p == 1):
            return self.pc

    def run(self):
        self.pc = 0
        while True:
            ins = str(self.code[self.pc]).zfill(5)
            opcode = int(ins[-2:])
            #print(self.pc,opcode)

            parameter_options = [int(p) == 1 for p in ins[:-2]][::-1]
            actual_params = [self.get_param(parameter_options[p]) for p in range(self.op_parameters[opcode])]

            if (opcode == 99):
                if (self.final_stream):
                    self.final_stream.put(self.last_output)
                #print("Program",self.name,"exiting")
                break

            self.ops[opcode](*actual_params)
            self.pc += 1

            #if (self.stop):
            #    break

    def set_input_stream(self,stream):
        self.input_stream = stream


f = open(sys.argv[1])
code = list(map(int,f.readline().strip().split(',')))

final = 0
#for inputs in [[9,8,7,6,5]]:
#for inputs in permutations([4,3,2,1,0]):
for inputs in permutations([5,6,7,8,9]):
    print("New input", inputs)
    inputs = list(inputs)

    a_q = Queue()
    a_q.put(inputs[0])
    a_q.put(0)

    b_q = Queue()
    b_q.put(inputs[1])
    c_q = Queue()
    c_q.put(inputs[2])
    d_q = Queue()
    d_q.put(inputs[3])
    e_q = Queue()
    e_q.put(inputs[4])

    f_q = Queue()

    a = Program(code, a_q, b_q)
    b = Program(code, b_q, c_q)
    c = Program(code, c_q, d_q)
    d = Program(code, d_q, e_q)
    e = Program(code, e_q, a_q, f_q)

    a_t = Process(target=a.run)
    b_t = Process(target=b.run)
    c_t = Process(target=c.run)
    d_t = Process(target=d.run)
    e_t = Process(target=e.run)

    a_t.start()
    b_t.start()
    c_t.start()
    d_t.start()
    e_t.start()

    while (e_t.is_alive()):
        pass
    #print("E exited")

    a_t.terminate()
    b_t.terminate()
    c_t.terminate()
    d_t.terminate()
    e_t.terminate()

    #print("Threads? exited")
    final = max(final,f_q.get())

print(final)

