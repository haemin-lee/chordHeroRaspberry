import requests
import RPi.GPIO as GPIO

url = 'https://chordhero-backend.herokuapp.com/'


ledPin = 21 
buttonPin = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(1):
    if GPIO.input(buttonPin): #button is pressed
        GPIO.output(ledPin, GPIO.HIGH)
        x = requests.get(url)
        print(x.text)
    else:
        GPIO.output(ledPin, GPIO.HIGH)