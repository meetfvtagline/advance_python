import requests 
r=requests.post("https://httpbin.org/post", data=[("name", "meet"), ("age", "24")])
print(r.text)
