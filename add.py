import requests

url = 'http://localhost:5000/uploadNewSong'
url2 = 'https://chordhero-backend.herokuapp.com/'
myobj = {'twinkletwinkle': [['C', 'D', 'F'], ['D', 'E', 'G'], ['C', 'F', 'A']]}

x = requests.post(url, data = myobj)

y = requests.get(url2, data = myobj)

print(x.text)
print(y.text)