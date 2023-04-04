import requests

response = requests.get('http://google.com')

# print(response.text)
print(response.content)

# r = requests.get('http://python.org/blabla')
# if r.status_code not in range(400, 600):
#     print('Pavyko prisijungti! Dirbame toliau...')
# else:
#     print(f'Kažkas ne taip.. Kodas {r.status_code}')