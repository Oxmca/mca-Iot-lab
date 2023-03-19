import time 
import RPi.GPIO as gpio 
gpio.setwarnings(False) 
gpio.setmode(gpio.BOARD) 
relay1 = 38 
gpio.setup(relay1,gpio.OUT,initial=0) 
try: 
    gpio.output(relay1, True) 
    print("Relay is Switched On. Please Press ctrl+c to exit") 
    time.sleep(15) 
    print("Relay is Switched Off.") 
    gpio.output(relay1, False) 
except KeyboardInterrupt: 
    gpio.cleanup() 
    print("Program Exited") 
print("")