  
## difference between tuple and list that the tuple is constant

tuple1=tuple() #empty tuple 
print(type(tuple),{tuple})

##convert from list to tuple 
tuple2=tuple([1,2,3])
print(tuple2)
print(type(tuple2))
tuple5=tuple(range(6))
print(tuple5)
# print(tuple)
# tuple=1,3,5
# print(type(tuple))
stringtuple=tuple("hello")

print(stringtuple)
print(type(stringtuple))
print(len(stringtuple))

stringtuple2=tuple({"hello"})

print(stringtuple2)
print(type(stringtuple2))
print(len(stringtuple2))
print("\n")

tuple12=(1,3,5,6,7,3,1,3)
first,*_,last=tuple12
print(first)
# print(middle)
print(last)
