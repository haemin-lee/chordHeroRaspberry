import requests

url = 'http://localhost:5000/uploadNewSong'
url2 = 'http://localhost:5000/getSong'
myobj1 = {'name': 'twinkletwinkle', 'keys': [['C', 'D', 'F'], ['D', 'E', 'G'], ['C', 'F', 'A']]}
myobj2 = {'name': 'silentnight', 'keys': [['C', 'D', 'F#'], ['D', 'E#', 'G'], ['C#', 'F', 'A']]}
myobj3 = {'name': 'jinglebells', 'keys': [['C', 'A', 'D'], ['D', 'F', 'B'], ['C', 'A', 'A#']]}

obj = {'id': '0'}

x = requests.post(url, json = myobj1)
y = requests.post(url, json = myobj2)
z = requests.post(url, json = myobj3)

a  = requests.post(url2, json=obj)


