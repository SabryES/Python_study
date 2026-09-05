# class person:
 
#     def __init__(self,name:str,age:int):
#         print("EHHHS")
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"name:{self.name},Age:{self.age}"
        
# mohamed=person("Sabry",34)
# # mohamed.name="sabry" ; mohamed.age=4
# print(mohamed.age)
# print(mohamed.name)
# print(mohamed)


# ##access private member
# class Data :
#     __myvar=10 #private member
#     var=123
#     def __init__(self) -> None:
#         print("Data object is created")

# data=Data
# print(data.var)
# # print(data.__myvar)#errror 
# print(data._Data__myvar)

#operator Overloading
# ##error for no operator overloading 
# class Number:
#     number = 0
#     def __init__(self,number) :
#         print("number class is created")
#         self.number=number

# number = Number(10)
# number2 = Number(30)

# result=number+number2
# print(result)
 
# ###solution for operator overloading

# class Number:
#     number = 0
#     def __init__(self,number) :
#         print("number class is created")
#         self.number=number
#     def __add__(self, other):
#         print("OPerator is overloaded")
#         return self.number+other.number
# number = Number(10)
# number2 = Number(30)

# result=number+number2
# print(result)


####functor 
class CallingCallable:
    def __init__(self,value) -> None:
        print("Con")
    def __call__(self) :
        print("caalliing")

obj=CallingCallable(11)
obj()  ##functor