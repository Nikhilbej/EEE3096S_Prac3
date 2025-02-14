# EEE3096S_Prac3
A repository for prac 3 from EEE3096S 2020

Explanation of code:

We used a wait time of 5 seconds to detect a falling or rising edge. Our code basically inverts the state of the LED pin whenever it detects an edge. So once the button is pushed and held for 5 seconds a rising edge is detected, the the LED is turned on. Then, when the button has been released for 5 seconds the LED is turned off because the GPIO pin is set low.Five seconds may be too long but we wanted to make sure that we are able to see the LED light up for some time.

A list of useful resources for this practical:
1. https://pinout.xyz/pinout/pin11_gpio17
2. http://acoptex.com/project/4006/project-19c-raspberry-pi-zero-w-board-led-and-push-button-at-acoptexcom/
3. https://raspberrypi.stackexchange.com/questions/83150/raspberry-pi-led-not-turning-on-with-button
4. https://www.makeuseof.com/tag/add-button-raspberry-pi-project/
5. https://www.hackster.io/hardikrathod/push-button-with-raspberry-pi-6b6928
6. http://wiki.ee.uct.ac.za/RaspberryPi:ProgrammingInPython
