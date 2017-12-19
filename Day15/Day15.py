#!/bin/python
import ctypes

remainder = 2147483647

factorA = 16807
factorB = 48271

generatorA = 591
generatorB = 393

#generatorA = 65
#generatorB = 8921

count = 0

def check16bits(valueA, valueB):
        return  (valueA & 0x0000FFFF) == ( valueB & 0x0000FFFF)
    

def doStep(lastvalue, factor):
    return (lastvalue * factor) % remainder


#auxA = generatorA
#auxB = generatorB
#for _ in range(40000000):
    #auxA = doStep(auxA, factorA)
    #auxB = doStep(auxB, factorB)
    ##print (auxA, auxB)
    #if (check16bits(auxA, auxB)):
            #count = count + 1
    
#print count

# Second part
auxA = generatorA
auxB = generatorB
count = 0

for _ in range(5000000):
    auxA = doStep(auxA, factorA)
    while ( (auxA % 4) != 0):
        auxA = doStep(auxA, factorA)
        
    auxB = doStep(auxB, factorB)
    while ( (auxB % 8) != 0):
        auxB = doStep(auxB, factorB)
    if (check16bits(auxA, auxB)):
            count = count + 1
    
print count
