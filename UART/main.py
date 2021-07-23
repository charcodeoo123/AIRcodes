 # ls /dev/tty* to find serial port for arduino
# python3 -m pip install pyserial
# sudo apt install python3-pip

#!/usr/bin/env python3
import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.flush()

    while True:
        temper =0
        file = open('my_file.csv', 'r')
        temper = file.read ()
        file.close()
        ser.write("Hello from Raspberry Pi!\n".encode('utf-8')) #testing
        ser.write(temper+"\n".encode('utf-8'))
        
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)

