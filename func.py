# functions - pre-defined, user defined-- def
# input(), print()

# syntax
# def function_name(parameters):  #parameters is the variable of the function
    # ------block of code--
    # ------block of code--

# a=10
# b=20
# def summs():
#     print(a+b)
      
# summs()


#function with parameter
# def sums(i,j,k):  # i,j is parameter
#     print(i+j)
    
# a=int(input("Enter a "))
# b=int(input("Enter b "))

# sums(a,b,23)  # a,b is arguments
# sums(12,15)

# def kuchbhi(i,j):
#     print(i+j)
    
# kuchbhi(12,13)


# function with return 

# def summ(i,j):
#     # print(i*j)
#     return i*j

# v= summ(11,12)
# print(v)

#function with default paramters

# def multi(i,j=5):
#     return i*j

# print(multi(11,12))


# function with keyword arguments

# def printing(a,b,c):
#     print(a,b,c)
    
# # i,j,k=10,20,30

# printing(c=10,b=20,a=30)

def oddEven(i):
    if i%2==0:
        return "Even"
    else:
        return "Odd"
    
# user= int(input("Enter value "))
# print(oddEven(user))


# Args , Kwargs

def summ(*a):
    # print(a)
    s=0
    for i in a:
        s+=i  # s=s+i
        
    print(s)
        
summ(12,13)
summ(12,13,34)
summ(12,13,34,67)
summ(12,13,34,67,89)

