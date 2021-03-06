import time
import board
import digitalio
import Adafruit_DHT

kaptonheaters = digitalio.DigitalInOut(board.D2)
kaptonheaters.direction = digitalio.Direction.OUTPUT
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

print ("System On")

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from DHT22")
while True:
    if temperature > 0:
        kaptonheater.value = True
        print ("Heating on")
    else:
        print ("Temperature okay")
