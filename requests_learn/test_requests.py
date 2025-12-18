import requests
res=requests.get('https://www.w3schools.com/python/module_requests.asp')
print(res.text)