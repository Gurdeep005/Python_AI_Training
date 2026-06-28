# What is Python?
#       Python is a high-level, interpreted, and general-purpose programming language that is easy to learn and use.
#       It was created by Guido van Rossum in 1991.

#  Features of Python
#       * Easy to learn
#       * Simple syntax
#       * Free and open source
#       * Platform independent
#       * Large number of libraries
#       * Used in AI, Machine Learning, Web Development, Data Science, Automation, etc.

#-------------------------------------------------------------------------------------------------------------------------

# How Python Works--  Python is an interpreted language.

# Working Process-
#        * Write Python code.
#        * Python Interpreter reads the code.
#        * Code is converted into Bytecode.
#        * Python Virtual Machine (PVM) executes the bytecode.
#        * Output is displayed.

#  Diagram-
#           Python Code
#                 ↓
#            Interpreter
#                 ↓
#             Bytecode
#                 ↓
#               PVM
#                 ↓
#              Output

#--------------------------------------------------------------------------------------------------------------------------

# Variables in Python--  A variable is a name used to store data in memory.

#  Rules for Naming Variables-
#      ✔ Can contain letters, digits and underscore
#      ✔ Cannot start with a digit
#      ✔ Cannot use keywords

#-------------------------------------------------------------------------------------------------------------------------

# Types of Cases in Python--  Naming conventions used in Python.

#  A. Snake Case--  Words separated by underscores.
#   eg-
#      * student_name
#      * total_marks
# Used most commonly in Python.

#  B. Camel Case--  First word starts with small letter and next words start with capital letters.
#   eg-
#      * studentName
#      * totalMarks

#  C. Pascal Case--  Every word starts with a capital letter.
#   eg-
#      * StudentName
#      * TotalMarks
# Used for class names.

#  D. Kebab Case--  Words separated by hyphens.
#  eg-
#       * student-name
# Not valid for Python variable names.

#  E. Upper Case--  All letters are capital and underscore between words.
#   eg-
#       * STUDENT_NAME
# Used for constants.

#----------------------------------------------------------------------------------------------------------------------------

# Datatypes:-

# Python Data Types-
#            ├── Numeric
#            │   ├── int
#            │   ├── float
#            │   └── complex
#            │
#            ├── Boolean
#            │
#            ├── Set
#            │
#            ├── Sequential
#            │   ├── list
#            │   ├── string
#            │   └── tuple
#            │
#            └── Dictionary

#---------------------------------------------------------------------------------------------------------------------------

# Errors in Python--  Errors are mistakes in a program.

#  A. Syntax Error-  Occurs when Python grammar rules are violated.
#   Example-
#          print("Hello"
#     Output:
#           SyntaxError

#  B. Runtime Error-  Occurs while executing the program.
#   Example:
#           a = 10
#           b = 0
#            print(a/b)
#    Output:
#          ZeroDivisionError

#  C. Logical Error-  Program runs but gives wrong output.
#   Example:
#          a = 10
#          b = 20
#          print(a-b)
#   Output:
#          -10
#  If addition was expected, this is a logical error.

#-----------------------------------------------------------------------------------------------------------------------------

# Type Conversion in Python--  Converting one data type into another data type is called Type Conversion.

# There are two types:
#  A. Implicit Type Conversion--  Python automatically converts data types.
#    Example:
#            a = 10
#            b = 5.5
#            c = a + b

#      print(c)
#      print(type(c))

#    Output:
#          15.5
#          <class 'float'>
# Python converts integer to float automatically.

#  B. Explicit Type Conversion (Type Casting)--  Programmer converts data type manually.
#    Example:
#             a=10
#             b=float(a)
#              print(b)
#              print(type(b))
#    Output:
#           10.0
#           <class'float'>