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
    buttonPin=13
    
    #Setting up the pins
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin,GPIO.IN)
    
    # wait for up to 5 seconds for an edge
    edge = GPIO.wait_for_edge(buttonPin, GPIO.BOTH, timeout=5000)
    if edge is None:
        pass
    else:
        GPIO.output(ledPin, not GPIO.input(LED))
    
  
    



        
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