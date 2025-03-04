# # variable swap using bitwise XOR

# # a = 5  
# # b = 10  

# # print("Before swapping:")  
# # print(f"a = {a}, b = {b}")  

# # # Swapping values using XOR  
# # a = a ^ b  # Step 1: a now holds the XOR of a and b  
# # b = a ^ b  # Step 2: b now holds the original value of a  
# # a = a ^ b  # Step 3: a now holds the original value of b  

# # print("After swapping:")  
# # print(f"a = {a}, b = {b}")

# a=10
# b=20

# # print(a^b)
# a= a^b  #-- 30
# b= b^a 
# a=a^b
# print("value of a is ",a)
# print("value of b is ",b)

# if else, elif

# a=int(input("Enter Value of a "))
# b=int(input("Enter value of b "))

# if a>b:
#     print("a is greater than b")
# elif a==b:
#     print("a is equal to b")
# else:
#     print("a is smaller than b")

# marks= int(input("Enter your marks "))

# if marks>=90 and marks<=100:
#     print("A")
# elif marks>=80 and marks<90:
#     print("B")
# elif marks>=70 and marks<80:
#     print("C")
# elif marks>=60 and marks<70:
#     print(marks)
# elif marks<60:
#     print("Fail")
# else:
#     print("Invalid Marks")
 
 
# for loop

# for(int i=0;i<10;i++){
#     printf(i)
# }

# for i in range(1,1000):   # start stop step
#     print(i)
    
    #start include in loop
    #stop exclude in loop (not included in loop)
    
# for i in range(4,15):
#     print("Gurminder",i)

# for i in range(15):  # start by default 0
#     print("Gurminder",i)


# for i in range(0,10,2):  # step +1
#     print("Gurminder",i)
# for i in range(10,0,-1):  # step +1
#     print("Gurminder",i)


# while loop
# i=0

# while i<30:
#     print('Hi',i)
#     i+=1 #or i=i+1
   
    
# print(i)

# break and continue


# a=5
# for i in range(0,10):
#     if i==5:
#         break
#     print(i)
for i in range(0,10):
    if i==5:
        continue
    print(i)

