import requests

url = 'https://chordhero-backend.herokuapp.com/uploadNewSong'
delete = 'https://chordhero-backend.herokuapp.com/deleteAll'
#url = 'http://localhost:5000/uploadNewSong'
#getSong = 'http://localhost:5000/getSong'
getSong = 'https://chordhero-backend.herokuapp.com/getSong'

myobj1 = {'url': 'https://www.youtube.com/watch?v=bvWRMAU6V-c&ab_channel=DisneyMusicVEVO', 'keys': ["AMajor", "DMinor"]}
myobj2 = {'url': 'https://www.youtube.com/watch?v=VF-r5TtlT9w&ab_channel=HarryStylesVEVO', 'keys': ["AMajor", "DMinor"]}
myobj3 = {'url': 'https://www.youtube.com/watch?v=Dwzk-XZxZ4k&ab_channel=KALIUCHIS', 'keys': ["AMajor", "DMinor"]}

one={'id':'0'}
#x = requests.get(delete)

'''x = requests.post(url, json = myobj1)
x = requests.post(url, json = myobj2)
x = requests.post(url, json = myobj3)'''

x = requests.post(getSong, json=one)


print(x.text)


