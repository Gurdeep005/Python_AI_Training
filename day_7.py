# INHERITANCE--

# class Parent:
#     def __init__(self,a,b):
#         print("The sum of a and b is: ",a + b)

#     def greet    

# class Child(Parent):
#     def __init__(self):
#         super().__init__(4,6)

# obj = Child()

# class Vehicle:
#     def __init__(self,a):
#         print("No. of tyres:", a)

#     def fuel(self,b):
#         print("Fuel type:", b)

# class Car(Vehicle):
#     def __init__(self,c,d):
#         print("Name of car: ", c)
#         print("Model of car: ", d)

#         super().__init__(4)
#         super().fuel('Diesel')            

# xuv = Car("xuv",2022)    

#----------------------------------------------------------------------------------------------------------------------------------------

# GETTER AND SETTER--

# class abc:
#     def __init__(self):
#         self._a = 0

#     @property
#     def value(self):
#         return self._a

#     @value.setter
#     def value(self,value):
#         self._value = value

# obj = abc()
# obj.value = 15 
# print(obj.value)           

#------------------------------------------------------------------------------------------------------------------------------------------

# FILE HANDLING--

# file = open("file.txt", "r")
# data = file.read()
# print(data)

# file = open("file.txt", "w")
# data = file.write("This is file")
# print(data)

# file.close()#deletes the extra assigned memory

# file = open("file.txt", "a")
# data = file.write("hello")
# print(data)

# file = open("file.txt", "r")
# data = file.readline()
# print(data)

# with open("file.txt", "r") as file:  #no need to close the file
#     data = file.read()
#     print(data)

# with open("test.png", "br") as file:
#     with open("png.txt", "bw") as file2:
#         file2.write(file.read())

#readlines----gives list of lines

with open("file.txt", "r") as file:
    content = file.readlines()
    print(content)
   
sum = 0
for line in content:
    value = int(line.split("=")[1])

    if value % 2 != 0:
        sum = sum + value

print("Sum of odd values =", sum)
