#!/bin/python

registers = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'p':0}
frequency = 0

def parseparm(param):
    if param.isalpha():
        return registers[param]
    else:
        return int(param)


def process_snd(line):
    global frequency
    #frequency = registers[line[4]]
    frequency = parseparm(line[4])
    print "   Sound: " + str(frequency)
    return 1

def process_set(line):
    registers[line[4]] = parseparm(line[6:50])
    return 1

def process_add(line):
    registers[line[4]] = registers[line[4]] + int(line[6:50])
    return 1

def process_mul(line):
    #registers[line[4]] = registers[line[4]] * registers[line[6]]
    registers[line[4]] = parseparm(line[4]) * parseparm(line[6:20])
    
    return 1

def process_mod(line):
    registers[line[4]] = registers[line[4]] % parseparm(line[6:20])
    return 1

def process_rcv(line):
    if registers[line[4]] != 0:
        print "   Freq: "+ str(frequency)
        return -999
    else:
        return 1

def process_jgz(line):
    if registers[line[4]]  != 0:
        return int(line[6:15]) 
    else: return 1

def process_line(line):
    #print line
    if "snd" in line:
        return process_snd(line)
    if "set" in line:
        return process_set(line)
    if "add" in line:
        return process_add(line)    
    if "mul" in line:
        return process_mul(line)    
    if "mod" in line:
        return process_mod(line)    
    if "rcv" in line:
        return process_rcv(line)    
    if "jgz" in line:
        return process_jgz(line)
   


#with open('testfile.txt') as f:
with open('input.txt') as f:
    lines = f.read().splitlines()
    
index = 0
aux = 0
while True:
    #print "Step: " + str(index)
    aux = process_line(lines[index])
    if aux == -999: break
    index = index + aux
    #print registers
    
print registers
print "Frequency: " + str(frequency)


