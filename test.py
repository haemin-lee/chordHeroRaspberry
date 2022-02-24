import requests

url = 'https://chordhero-backend.herokuapp.com/'

x = requests.get(url)

print("hello please work")
print(x.text)