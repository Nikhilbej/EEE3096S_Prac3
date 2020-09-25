#Importing modules to be used
import RPi.GPIO as GPIO
import time
#Declaring our main function
def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    ledPin = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.HIGH)
    #delay for 5 seconds to notice the LED toggling
    time.sleep(5)
    #Setting the LED low
    GPIO.output(ledPin, GPIO.LOW)
    #Cleanup any unused resources
    GPIO.cleanup()


        
#only run functions if this module is run
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
    except Exception as e:
        print("Error: {}".format(e))