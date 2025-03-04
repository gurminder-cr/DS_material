# {}, key-value pair

d={'name':'Gurminder','class':'btech','roll':1234,'isownapet':False}
print(d)

# print(d['name'])
# print(d['class'])
# print(d['classs'])

print(d.get('classs','Not present')) #return the value for key if key is in the dictionary, else default message

i=set()
# i={}
# print(type(i))
# print(i)
# i.update([12,13,True,'hi',1])
# print(i)


# d.update(name='Manisha')
# print(d)
# d.update(college='GNIEM')
# print(d)

d['name']='Mohit'
print(d)
d['college']='SBSS'
print(d)


# d.pop('rolls')
# print(d) 

print(d.keys())
print(d.values())
print(d.items())


# for i in d.items():
#     print(i)
for i,j in d.items():
    print(i,"==",j)