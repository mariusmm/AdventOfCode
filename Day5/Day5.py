#!/bin/python

def runmachine_1(my_list):
    jump = 0
    index = 0
    steps = 0
    index_new = 0
    while index<len(my_list):
        #print (index, index_new)
        index_new = my_list[index]
        if (index >= len(my_list)) or (index < 0): 
            break
        my_list[index] = my_list[index] + 1
        steps = steps + 1
        index = index_new+index
    return steps

def runmachine_2(my_list):
    jump = 0
    index = 0
    steps = 0
    index_new = 0
    while index<len(my_list):
        index_new = my_list[index]
        if (index >= len(my_list)) or (index < 0): 
            break
        if (index_new >= 3):
            my_list[index] = my_list[index] - 1
        else:
            my_list[index] = my_list[index] + 1
        
        steps = steps + 1
        index = index_new + index
    return steps

test_list = [0, 3,  0,  1,  -3]

with open("input.txt") as f:
    lines = f.read().splitlines()

# 1st test
my_list = list(map(int, lines))
print "Day5 1st: " + str(runmachine_1(my_list))

# 2nd test
my_list = list(map(int, lines))
print "Day5 2nd: " + str(runmachine_2(my_list))
