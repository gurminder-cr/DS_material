# []- square brackets ,indexed, ordered, mutable(can change), heterogenous(all types of data)

li=[12,'hi',True,45.5,33,17,33]
# print(li)

#indexed
# print(li[2])
# print(len(li))
 
#slicing 
# print(li[:])  # start stop step  
# print(li[:5])    
# print(li[1:2])    
# print(li[::2])
# print(li[::-1]) # reverse list

# print(li[2:5:-1])
# print(li[5:2:-1])



#list update 
print(li)
li[1]=False
print(li)

li.append('st')  # add on last 
# li.append([31,32])  # add on last 
# print(li)

li.extend([22,32])
print(li)

li.pop()  #index by default-last Remove and return item at index (default last).Raises IndexError if list is empty or index is out of range
li.pop(5)  #index by default-last Remove and return item at index (default last).Raises IndexError if list is empty or index is out of range
print(li)

li.remove(True)  # remove first occurence of value
print(li)

li.insert(4,'hello') # index, value
print(li)

# li.sort()
n=[12,45,11,9,5,49,90,8]
n.sort()
print(n)

# for i in li:
#     print(i)

