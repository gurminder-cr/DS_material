# list comprehension

# li=[2,3,4,5,6,7,8,9,12,15,13,18,19,21,23,24,26,27]
# new_list=[]
# for i in li:
#     # print(i)
#     if i%3==0:
#         new_list.append(i)
# print(new_list)


li=[2,3,4,5,6,7,8,9,12,15,13,18,19,21,23,24,26,27]

# for i in range(10):
#     print(i)
# n=[i for i in range(10)]
# n=[i for i in li if i%3==0]
# print(n)
        
n=[i if i%3==0 else i**2 for i in li ]
# print(n)



li1=[1,2,3,4,5]
li2=[3,4,5,6,7]

#---  [3,4,5]
#--- [(3,3),(4,4),(5,5)]
# for i in li1:
#     for j in li2:
#         if i==j:
#             print(i)

# li=[(i,j) for i in li1 for j in li2 if i==j]
# print(li)




        


    