import time 
import RPi.GPIO as gpio 
gpio.setwarnings(False) 
gpio.setmode(gpio.BOARD) 
led1 = 15 
gpio.setup(led1,gpio.OUT,initial=0) 
file1 = open('ledintervals.txt', 'r') 
Lines = file1.readlines() 
ON_TIME = int(Lines[0].split("=")[1]) 
OFF_TIME = int(Lines[1].split("=")[1]) 
try: 
    while(True): 
        gpio.output(led1,True) 
        time.sleep(ON_TIME) 
        gpio.output(led1,False) 
        time.sleep(OFF_TIME) 
except KeyboardInterrupt: 
    gpio.cleanup() 
print("") 