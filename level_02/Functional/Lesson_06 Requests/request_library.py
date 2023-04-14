# https://github.com/robotautas/kursas/wiki/Requests

import requests

# Pagrindines komandos
"""
requests.get # pima is serverio duomenis
print(dir(response)) # parodo objekto response metodus
print(response.text) # grazina puslapio turini HTML formatu
print(response.content) # grazina turini binary formatu
print(r.status_code) # status_code isspauzdina serverio response
if r.ok: #grazina True ar false
headers .headers grąžina mums papildomus duomenis apie atsaką (response)
print(r.url) # aspauzdina koki naudojame url
"""


# response = requests.get('http://google.com')
# # responce yra objektas

# print(dir(response)) # parodo objekto response metodus
# # print(response.text) # grazina puslapio turini HTML formatu
# # print(response.content) # grazina turini binary formatu

# get matodas gauna bunary paveiksliuka ir ji irasome i faila
"""
r = requests.get('https://www.python.org/static/img/python-logo.png')
print(r.content)

with open('logo.png', 'wb') as f:
    f.write(r.content)

"""
"""
r = requests.get('http://python.org')
print(r.status_code)
# status_code isspauzdina serverio response
"""

"""
# r = requests.get('http://python.org/blabla')
# if r.status_code not in range(400, 600):
#     print('Pavyko prisijungti! Dirbame toliau...')
# else:
#     print(f'Kažkas ne taip.. Kodas {r.status_code}')
"""

###################
# URL parammetrai:
###################
# http://www.httpbin.org/
###################


# HTTP: metodai:
# get, post, delete, patch.
"""
r = requests.get('https://www.python.org/search/?q=pep')
print(r.text)

payload = {'q': 'pep', 'page': '2'}
r = requests.get('https://www.python.org/search/', params=payload)
print(r.url)
# https://www.python.org/search/?q=pep&page=2
"""

r = requests.get('http://httpbin.org/ip')
print(r.text)
# {
#   "origin": "78.63.103.114, 78.63.103.114"
# }

data = {'name': 'Jonas', 'lastname': 'Jonaitis'}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
# ... 
# "form": {
#     "lastname": "Jonaitis", 
#     "name": "Jonas"
#   }, 
#  ...