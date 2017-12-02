#!/bin/python

import csv

def doMath(mylist):
    results = list(map(int, mylist))
    mymax = max(results)
    mymin = min(results)
    #print "Max: " + str(mymax) + " Min: " + str(mymin)
    return mymax - mymin
    
def doMath2(mylist):
    results = list(map(int, mylist))
    for i in results:
        for j in results:
            if (i == j): break
            if (i % j) == 0:
                result = i / j
            if (j % i) == 0:
                result = j / i
    return result
       
## Firsst part 
result = 0  
#with open('inputtest.txt', 'rb') as csvfile:
with open('input.txt', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        #print row
        result = result + doMath(row)        
    print "1: " + str(result)

## Second part
result = 0
with open('input.txt', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        result = result + doMath2(row)
    print "2: " + str(result)
