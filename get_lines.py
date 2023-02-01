import requests

server = input()
port = input()
a = input()
b = input()

response = requests.get(f'{server}:{port}', params={
    'a': a,
    'b': b,
})
data = response.json()
print(*sorted(data['result']))
print(data['check'])
