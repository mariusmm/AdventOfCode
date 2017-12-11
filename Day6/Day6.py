#!/bin/python

input_list=[4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
#input_list=[0, 2, 7, 0]
#input_list=[2, 4, 1, 2]
length= len(input_list)
final_list = []

    
def redistribute(in_list):
    max_value = max(in_list)
    max_index = in_list.index(max_value)    
    index = max_index
    in_list[max_index]=0
    for count in range(0, max_value):
        index = (index + 1) % length
        in_list[index] = in_list[index] + 1
        #print str(count) + ". index: " + str(index) + ": " + str(in_list)
        #print input_list
    return in_list


counter = 0
while True:
    input_list = redistribute(input_list)
    #print "I: " + str(input_list)
    #print "F: " + str(final_list)
    #print "********"
    counter = counter + 1
    if input_list in final_list:
        break
    final_list.append(list(input_list))

#print final_list    
print "counter: " + str(counter)
    
    


