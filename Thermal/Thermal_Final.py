#!/usr/bin/python3
import os
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import csv
import serial

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

MOSFET = 17
DHT_PIN = 4

GPIO.setup(MOSFET, GPIO.OUT)
DHT_SENSOR = Adafruit_DHT.DHT22

print ("System On")
try:
    f = open('/home/pi/humidity.csv', 'a+')
    if os.stat('/home/pi/humidity.csv').st_size == 0:
            f.write('Date,Time,Temperature,Humidity\r\n')
except:
    pass

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
        f.flush()
        #print("Michael")
    else:
        print("Failed to retrieve data from humidity sensor")
    def get_temp():
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

            if humidity is not None and temperature is not None:
                print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
                return temperature
            else:
                print("Failed to retrieve data from DHT22")

        datafile = open('humidity.csv', 'r')
        myreader = csv.reader(datafile)

        for row in myreader:
            print(row[0], row[1], row[2], row[3], row[4])
        if __name__ == '__main__':
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            ser.flush()

    temperature=get_temp()
    if temperature <= 0: #For testing, shall switch
        GPIO.output(17, GPIO.HIGH)
        print ("heat is on")
    else:
        GPIO.output(17, GPIO.LOW)
        print ("heat not on")

    time.sleep(5)
