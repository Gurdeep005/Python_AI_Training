#EXCEPTION HANDLING--

# try:    
#     pass
# except:
#     pass
# finally:
#     pass

# try:
#     print(6/0)
# except Exception as e:
#     print(e)
#     pass

# print("hello")


# try:
#     file = open("file,txt", "r")
#     print(file.read)
#     print("abc")

# except Exception as e:
#     print(e)

# finally:
#     file.close()    

# try:
#     print(6/0)
# except ZeroDivisionError:
#     print("You cannot do this")

# except TypeError:
#     print("Types must be same")

# except Exception:
#     print("Something went wrong")


# try:
#     a = int(input("Enter an even number: "))
#     if (a%2 != 0):
#         raise Exception()

# try:
#     a =int(input("Enter your age: "))
#     if (a < 18):
#         raise Exception("You are not eligible to vote")
    
#     elif (a >= 18 and a < 110):
#         print("You are eligible to vote")
    
#     elif (a > 110):
#         raise Exception("You are invalid to vote")
# except ValueError:
#     print("Age must be integer")   
# except Exception as e:
#     print(e)

#-------------------------------------------------------------------------------------------------------------------------------------------

# API--
# from urllib.request import Request, urlopen   #urllib= folder which contains files=Request, urlopen

# req = Request(url='https://jsonplaceholder.typicode.com/posts', method="GET")
# response = urlopen(req)
# print(response.read())

# from urllib.request import Request, urlopen   #urllib= folder which contains files=Request, urlopen
# req = Request(url='https://jsonplaceholder.typicode.com/posts/80', method="GET")
# response = urlopen(req)
# print(response.read())

# from urllib.request import Request, urlopen   #urllib= folder which contains files=Request, urlopen
# req = Request(url='https://jsonplaceholder.typicode.com/posts/80/comments', method="GET")
# response = urlopen(req)
# print(response.read())


import requests
res = requests.get('https://jsonplaceholder.typicode.com/posts')
print(res)  #[200]=ok ,401=unauthorized, 404=not found(wrong route), 500=internal server error

#methods==get, post, put, patch, delete