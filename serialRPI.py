#!/usr/bin/env python3
import requests
import RPi.GPIO as GPIO
import serial
import time
url = 'https://chordhero-backend.herokuapp.com/getSong'

one = {'id': '0'}
two = {'id': '1'}
three = {'id': '2'}

ledPin = 21 
button1Pin = 20
button2Pin = 26
button3Pin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(button1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


if __name__=='__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    
    while True:
        if GPIO.input(button1Pin) == 0: #button2 is pressed
            print("2")
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(ledPin, GPIO.HIGH)
            a  = requests.post(url, json=two)
            print(a.text)
        #requests.post(url, data = song1)
        #upload song 1
            print(a.text[1])

            ser.write(b"Hi from rpi!\n")
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1)
