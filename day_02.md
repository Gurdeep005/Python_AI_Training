# Python Fundamentals — Notes

## What is Python?

**Python** is a high-level, interpreted, and general-purpose programming language that is easy to learn and use. It was created by **Guido van Rossum** in **1991**.

### Features of Python
- Easy to learn
- Simple syntax
- Free and open source
- Platform independent
- Large number of libraries
- Used in AI, Machine Learning, Web Development, Data Science, Automation, etc.

---

## How Python Works

Python is an **interpreted language** — code is executed line by line rather than compiled all at once ahead of time.

### Working Process
1. Write Python code
2. Python Interpreter reads the code
3. Code is converted into **Bytecode**
4. **Python Virtual Machine (PVM)** executes the bytecode
5. Output is displayed

**Flow diagram:**

```
Python Code
     ↓
 Interpreter
     ↓
  Bytecode
     ↓
    PVM
     ↓
  Output
```

---

## Variables in Python

A **variable** is a name used to store data in memory.

### Rules for Naming Variables
| Rule | Status |
|---|---|
| Can contain letters, digits, and underscores | ✅ Allowed |
| Can start with a digit (e.g. `1name`) | ❌ Not allowed |
| Can use reserved keywords (e.g. `class`, `if`) | ❌ Not allowed |

---

## Types of Naming Cases in Python

Naming conventions used to write variable, function, and class names consistently.

| Case Type | Rule | Example | Common Use |
|---|---|---|---|
| **Snake Case** | Words separated by underscores | `student_name`, `total_marks` | Most common — variables & functions in Python |
| **Camel Case** | First word lowercase, next words capitalized | `studentName`, `totalMarks` | Common in JS/Java; less common in Python |
| **Pascal Case** | Every word capitalized | `StudentName`, `TotalMarks` | Python class names |
| **Kebab Case** | Words separated by hyphens | `student-name` | ❌ Not valid for Python identifiers |
| **Upper Case** | All capitals, underscore-separated | `STUDENT_NAME` | Constants |

> 💡 **Tip:** Python's official style guide (PEP 8) recommends `snake_case` for variables/functions and `PascalCase` for classes.

---

## Python Data Types

```
Python Data Types
        │
        ├── Numeric
        │     ├── int
        │     ├── float
        │     └── complex
        │
        ├── Boolean
        │
        ├── Set
        │
        ├── Sequential
        │     ├── list
        │     ├── string
        │     └── tuple
        │
        └── Dictionary
```

| Category | Types | Example |
|---|---|---|
| Numeric | `int`, `float`, `complex` | `10`, `10.5`, `2+3j` |
| Boolean | `bool` | `True`, `False` |
| Set | `set` | `{1, 2, 3}` |
| Sequential | `list`, `string`, `tuple` | `[1,2]`, `"hi"`, `(1,2)` |
| Mapping | `dict` | `{"key": "value"}` |

---

## Errors in Python

An **error** is a mistake in a program that prevents it from running correctly.

### A. Syntax Error
Occurs when Python's grammar rules are violated.

```python
print("Hello"
```
**Output:**
```
SyntaxError: unexpected EOF while parsing
```

### B. Runtime Error
Occurs *while* the program is executing — the syntax is valid, but something goes wrong during execution.

```python
a = 10
b = 0
print(a / b)
```
**Output:**
```
ZeroDivisionError: division by zero
```

### C. Logical Error
The program runs successfully but produces the **wrong output** — there's no error message, just incorrect logic.

```python
a = 10
b = 20
print(a - b)
```
**Output:**
```
-10
```
> If addition (`a + b`) was actually expected, this is a **logical error** — Python won't flag it since the code is technically valid.

### Summary Table

| Error Type | When it Occurs | Detected By | Example |
|---|---|---|---|
| Syntax Error | Before execution | Interpreter (parsing stage) | Missing bracket |
| Runtime Error | During execution | Interpreter (execution stage) | Division by zero |
| Logical Error | After execution | Not detected automatically — only by the programmer | Wrong formula |

---

## Type Conversion in Python

**Type Conversion** is converting one data type into another.

### A. Implicit Type Conversion
Python automatically converts a data type to another **without programmer intervention**, usually to avoid data loss.

```python
a = 10
b = 5.5
c = a + b

print(c)
print(type(c))
```
**Output:**
```
15.5
<class 'float'>
```
Python automatically converts the `int` to a `float` so no precision is lost.

### B. Explicit Type Conversion (Type Casting)
The programmer manually converts a data type using built-in functions like `int()`, `float()`, `str()`.

```python
a = 10
b = float(a)

print(b)
print(type(b))
```
**Output:**
```
10.0
<class 'float'>
```

### Quick Comparison

| Aspect | Implicit | Explicit |
|---|---|---|
| Who performs it | Python (automatically) | Programmer (manually) |
| Function used | None | `int()`, `float()`, `str()`, etc. |
| Risk of data loss | Low (Python handles it safely) | Possible (e.g. `int(5.9)` → `5`) |
| Example | `int + float → float` | `float(10) → 10.0` |
