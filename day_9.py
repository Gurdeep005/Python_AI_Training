# API Calls with Python (requests)--

# www.google.com/Posts?userId=1
#before .com ---domain
#/posts---endpoint(where we are in website)
#?userId----params(after ?)query(we can add wrong query, it will not give 404 error)

# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response._content)
# print(response.cookies)
#print(response.status_code)
# print(response.elapsed)
# for key in response.headers.items():
#     print(key)
# elapsed -- time taken from request to response
# b = byte format
#frontier models -- take money to use their services

# import requests
# try:
#    response = requests.post("https://jsonplaceholder.typicode.com/posts", data={"title":"test","body": "test body", "userId": 999})
#    print(response.json())
#    response.raise_for_status()
# except Exception as e:
#    print(e)
#always wrap API calls in try except block and use this too ---.raise_for_status()

# import requests
# try:
#     response = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId":1})
#     print(response.json())
#     response.raise_for_status()
# except Exception as e:
#     print(e)

# import requests
# try:
#     response = requests.put("https://jsonplaceholder.typicode.com/posts/1", data={id: 1, "title": "test", "body": "aedh","userId": 444})
#     print(response.json())
#     response.raise_for_status()
# except Exception as e:
#     print(e)

# put---changes the whole object
# patch---changes the particular argument and parameter in an object

# curl http://192.168.1.2.11434 -d '{
#    "model": "phi3:latest",
#   "prompt": "Why is the sky blue?"
# }'