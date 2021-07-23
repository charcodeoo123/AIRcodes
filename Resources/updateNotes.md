# AIRcodes
Progress status:
 - DHT22 95%
 - kapton heaters 95%
 - cosmic watch 40% (transmitting data to Pi 3 and/or retrieving data from the sd card)
 - blv interface 50% (USB connection) Serial library
 - Storing data into SD card 20%

Further testing needed:
 - cosmic watch should work properly and collect consistent data
 - SD card should have a stable, consistent data with very little outliers
 - heaters should be turned on when requested



Setup:
install both python 3 and pip.
Library needed:
-os
-Time
-Adafruit_DHT
-I2C library(WiringPi)
To be continued...


MOSFET gate opens for LED, LED light turns on with the code, not for the KH.
Thermal 5 code(LED): 
(1) current - 0.35A voltage - 5V
(2) current - 3A    voltage - 5V using multimeter
LED/pwr supply shorted when using multimeter

LED lights start out dimmed without resistor, lights keep brightening
