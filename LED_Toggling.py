#Importing modules to be used
import RPi.GPIO as GPIO
import time
#Declaring our main function
def main():
    #Turning off warnings
    GPIO.setwarnings(False)
    #Setting the mode
    GPIO.setmode(GPIO.BOARD)
    #Choosing the pin for the LED
    ledPin = 11
    #Setting up the pin
    GPIO.setup(ledPin, GPIO.OUT)
    #Setting the LED pin high
    GPIO.output(ledPin, GPIO.HIGH)
    #delay for 5 seconds to notice the LED toggling
    time.sleep(5)
    #Setting the LED low
    GPIO.output(ledPin, GPIO.LOW)



        
#only run functions if this module is run
if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
    except Exception as e:
        print("Error: {}".format(e))
        #Cleanup any unused resources
        GPIO.cleanup()