#!/usr/bin/env python3
import requests
import RPi.GPIO as GPIO
import serial
import time
import json
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

chordDict= {"A:maj":["C#", "E", "A"], "A:min":["C","E","A"], "B:maj":["D#","F#","B"], "B:min":["D","F#","B"], "C:maj":["C","E","G"], "C:min":["C","D#","G"], "D:maj":["D","F#","A"], "D:min":["D","F","A"], "E:maj":["E","G#","B"], "E:min":["E","G","B"], "F:maj":["C","F","A"], "F:min":["C","F","G#"], "G:maj":["D","G","B"], "G:min":["D","G","A#"]}
keyDict= {"C": 0, "C#": 15, "D":16, "D#":31, "E": 32, "F":47, "F#":48, "G": 63, "G#": 64, "A":79, "A#":80, "B": 95}

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
            json_object = json.loads(a.text)
            print(a.text)
        #requests.post(url, data = song1)
        #upload song 1
            print(json_object["url"])
            array = json_object["keys"]
            
            serialString = "1.7|"
            
            for i in array:
                if i != "N":
                    temp = chordDict[i]
                    
                    for j in range(3):
                        serialString += str(keyDict[temp[j]])
                        if j != 2:
                            serialString += ","
                        else:
                            serialString += "|"
            print(serialString)
                        

            ser.write(b"Hi from rpi!\n")
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1)
