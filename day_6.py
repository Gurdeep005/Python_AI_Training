# ARGS--
# def hello(a, *args, b):
#     print("First argument:", a)
#     print("Second argument:", *args)
#     print("otherargument:", b)

#---------------------------------------------------------------------------------------------------------------------------------------

# KWARGS--
# hello(1, 2,2,3,4,5,b=6)    
    
# def hello(**kwargs):
#     print(type(kwargs))
#     sum = 0
#     for x in kwargs.values():
#         sum += x
#         print(sum)
#         print(kwargs)

#  hello(a=1, b=2, c=6)   

# def abc(**kwargs):
#     print(kwargs["key"])
    
# data = {"key": {"key": 7}}
# abc(**data)    

#--------------------------------------------------------------------------------------------------------------------------------------------

# LAMBDA--
# a = lambda x: x + 1
# x = int(input("Enter a number:"))
# print(a(x))

# def abc():
#     a = lambda x:x+1
#     b = lambda y:y+1
#     return a, b

# c = abc()
# print(c[0](5), c[1](8))

#----------------------------------------------------------------------------------------------------------------------------------------

# USING SELF METHOD--
# class car():
#     def __init__(self):
#        print("Car is created")

# c = car()       

# class car():
#     def __init__(self,a,b):
#        print("Car is created", a)
#        print("Car is created", b)

# c = car(1,2)    

# class calculator():
#     def add(self,a,b):
#         c = a+b
#         print("Sum is:",c)

#     def sub(self,a,b):
#         c = a-b
#         print("Difference is:",c)

# d = calculator()
# d.add(1,5)
# d.sub(1,5)

#----------------------------------------------------------------------------------------------------------------------------------------

# USING @STATIC METHOD--
class abc():
    @staticmethod
    def add():
        print("hello")

a = abc()
a.add()        
