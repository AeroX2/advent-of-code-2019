import sys
#from queue import Queue
from threading import Thread
from multiprocessing import Process, Queue
from itertools import permutations

class Program:
    def __init__(self,
                 code,
                 final_stream=None,
                 name=''):
        self.ops           = [self.nop, self.add, self.mul, self.inp, self.out, self.jt, self.jf, self.lt, self.eq, self.cro]
        self.op_parameters = {0:0, 1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 9:1, 99:0}

        #self.stop = False
        self.relative_offset = 0
        self.last_output = None

        self.code = code.copy()

        self.final_stream = final_stream
        self.name = name

    def nop(self):
        pass

    def add(self,a,b,c):
        self.code[c] = self.code[a]+self.code[b]

    def mul(self,a,b,c):
        self.code[c] = self.code[a]*self.code[b]

    def inp(self,a):
        self.code[a] = int(input("Input: "))

    def out(self,a):
        print(self.code[a])

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

    def cro(self,a):
        self.relative_offset += self.code[a]

    def get_param(self,p):
        self.pc += 1
        if (p == 0):
            return self.code[self.pc]
        elif (p == 1):
            return self.pc
        elif (p == 2):
            return self.relative_offset+self.code[self.pc]

    def run(self):
        self.pc = 0
        while True:
            ins = str(self.code[self.pc]).zfill(5)
            opcode = int(ins[-2:])

            #print(self.code[self.pc],end=' ')

            parameter_options = [int(p) for p in ins[:-2]][::-1]
            actual_params = [self.get_param(parameter_options[p]) for p in range(self.op_parameters[opcode])]

            if (opcode == 99):
                if (self.final_stream):
                    self.final_stream.put(self.last_output)
                #print("Program",self.name,"exiting")
                break

            #debug = ['nop','add','mul','inp','out','jt','jf','lt','eq','cro']
            #print(self.relative_offset,end=' ')
            #print(debug[opcode],end=' ')
            #print(parameter_options,end=' ')
            #print(actual_params,end=' ')
            #print([self.code[p] for p in actual_params])

            self.ops[opcode](*actual_params)
            self.pc += 1

            #if (self.stop):
            #    break

    def set_input_stream(self,stream):
        self.input_stream = stream


f = open(sys.argv[1])
code = list(map(int,f.readline().strip().split(',')))+[0]*10000
Program(code).run()
