import requests

url = 'https://chordhero-backend.herokuapp.com/'
myobj = {'twinkletwinkle': [['C', 'D', 'F'], ['D', 'E', 'G'], ['C', 'F', 'A']]}

x = requests.post(url, data = myobj)

print(x.text)