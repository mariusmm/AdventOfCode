#!/bin/python

test_string_1 = "aa bb cc dd ee" #True
test_string_2 = "aa bb cc dd aa" #False
test_string_3 = "aa bb cc dd aaa" #True

test_string_4 = "abcde fghij" #True
test_string_5 = "abcde xyz ecdab" #False
test_string_6 = "a ab abc abd abf abj" #True
test_string_7 = "iiii oiii ooii oooi oooo" #True
test_string_8 = "oiii ioii iioi iiio" #False

def checkvalid_1(mystring):
    array = mystring.split(" ")
    for word in array:
         if len([i for i,x in enumerate(array) if x==word]) > 1:
             return False
    return True

def checkvalid_2(mystring):
    array = mystring.split(" ")
    array2=[]
    for word in array:
        word2 = "".join(sorted(word))
        array2.append(word2)
    print array2
    
    for word in array2:
        print word
        if len([i for i,x in enumerate(array2) if x==word]) > 1:
             return False
    return True

# Day4 1st part

#print checkvalid(test_string_1)
#print checkvalid(test_string_2)
#print checkvalid(test_string_3)

counter = 0
with open("input.txt") as f:
    array = []
    for line in f:
        result = checkvalid_1(line.strip())
        if  result == True:  
            counter = counter+1
print "Day 4 1st: " + str(counter)

# Day4 2nd part
print "True::" + str(checkvalid_2(test_string_4))
print "False::" + str(checkvalid_2(test_string_5))
print "True::" + str(checkvalid_2(test_string_6))
print "True::" + str(checkvalid_2(test_string_7))
print "False::" + str(checkvalid_2(test_string_8))

counter = 0
with open("input.txt") as f:
    array = []
    for line in f:
        result = checkvalid_2(line.strip())
        if  result == True:  
            counter = counter+1
print "Day 4 2nd: " + str(counter)
