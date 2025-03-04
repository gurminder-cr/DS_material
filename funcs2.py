# kwargs
# def func1(**a):
#     print(a)
    



# func1(a=10,b=20)
# func1(a=10,b=20,c=30,d=40)
# func1(a=10,b=20,c=30,d=40,e=44)

#lambda functions

def main(a,b):
    # print(a+b)
    return a+b
# main(11,12)


# m = lambda a,b: print(a+b)
# m(11,12)

# m = lambda a,b: a+b
# print(m(11,14))

# def oddEven(a):
#     if a%2==0:
#         return "Even"
#     else:
#         return "Odd"
# oddEven(12)

# oe= lambda a:"Even" if a%2==0 else "Odd"
# print(oe(11))


#map 

l1=[1,2,3,4,5]
l2=[11,12,14,15,16]

# def check(a):
#     for i in a:
#         return i+5
# check(l1)

# def ad(a):
#     return a+2

# c = map(ad,[1,2,3,4,5])  # function, *iterables
# c = map(lambda a:a+2,[1,2,3,4,5])  # function, *iterables
# print(c)
# print(list(c))

# c = map(lambda a,b:a+b,[1,2,3,4,5],[2,3,4,5,6,7,8])  # function, *iterables
# print(c)
# print(list(c))


# filter 

# fil= filter(lambda a:True if a<35 else False, [33,37,38,23,36])
# print(list(fil))


l1=[1,2,3,4,5]
l2=[11,12,14,15,16]
# for i in zip(l1,l2):
#     print(i)
for i,j in zip(l1,l2):
    print(i+j)