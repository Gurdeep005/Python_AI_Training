# Introduction to Programming with Python--

# Simple calculator-
c = input("Enter operand: ")

while c != "QUIT" and c!="quit":
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))
    if c == "+":
        print(a+b)
    elif c =="-":
        print(a-b)
    elif c =="*":
        print(a*b)
    elif c =="/":
        print(a/b)
    elif c =="%":
        print(a%b)
    c = input("Enter operand: ")