import requests
import RPi.GPIO as GPIO
import time
url = 'https://chordhero-backend.herokuapp.com/'


ledPin = 21 
button1Pin = 20
button2Pin = 26
button3Pin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(button1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(1):

    if GPIO.input(button1Pin) == 0: #button2 is pressed
        print("1")
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(ledPin, GPIO.HIGH)
        #requests.post(url, data = song1)
        #upload song 1

    elif GPIO.input(button2Pin) == 0: #button2 is pressed
        print("2")
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(ledPin, GPIO.HIGH)
        #requests.post(url, data = song2)
        #upload song 2

    elif GPIO.input(button3Pin) == 0: #button3 is pressed
        print("3")
        GPIO.output(ledPint, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(ledPin, GPIO.HIGH)
        #requests.post(url, data = song3)
        #upload song 3
	
    else:
        GPIO.output(ledPint, GPIO.LOW)
        
