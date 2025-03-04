# Module or libraries dicussion 
#include<stdio>
#import 


# Exception handling


# import new 
# import random 


# print(random.randint(1,50)) # randint Return random integer in range [a, b], including both end points.


# # list random 

# a=['red','grey','black','green','orange','pink','blue']

# # print(random.choice(a))
# print(random.choices(a,k=2))


# import func3 

# i=int(input("Enter i "))
# ans= func3.evenOdd(i)
# print(ans)


# **kwargs -- functions 
# *args -- arbitrary arguments 


# def exampleFunc(*a):
#     print(a)
#     s=0
#     for i in a:
#         s+=i # s=s+i
#     print(s)
    
    
# exampleFunc(12)
# exampleFunc(12,23)
# exampleFunc(12,23,34)
# exampleFunc(12,23,34,67)


# **kwargs

def funcc(**a):
    print(a)
    print(a.values())
    for i in a.values():
        print(i)
    
# funcc(10,20,30)
# funcc(c=10,b=20,a=30)
# funcc(c=10,b=20,a=30,d=40)
# funcc(c=10,b=20,a=30,d=40,e=50,f=60)



# formatted string -- f strings

name="Gurminder"
age=23

print("My name is",name,"and age is",age)
print(f'My name is {name} and age is {age}')