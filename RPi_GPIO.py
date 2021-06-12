import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
#To set up a channel as an input or output
#GPIO.setup(channel, GPIO.IN)
#GPIO.setup(channel, GPIO.OUT)
GPIO.input(channel) #Reading the value of the channel
GPIO.output(channel, state) #To set the output state of a GPIO pin \ GPIO.output(led, GPIO.LOW)
GPIO.cleanup()#free up resources 
#!/usr/bin/python3
time.sleep(0.2)
