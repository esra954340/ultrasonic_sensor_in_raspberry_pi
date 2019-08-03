import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24

print("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

def measure():
        GPIO.output(TRIG, False)
        print("Waiting For Sensor To Settle")
        time.sleep(.5)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
                pulse_start = time.time()

        while GPIO.input(ECHO)==1:
                pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        print("Distance:",distance,"cm")
        
        if distance < 20 :
                print("LED on")
                GPIO.output(18,GPIO.HIGH)
                GPIO.output(22,GPIO.HIGH)
                time.sleep(1)
                print("LED off")
                GPIO.output(18,GPIO.LOW)
                GPIO.output(22,GPIO.LOW)
        else:
            GPIO.output(27,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(27,GPIO.LOW)

while True:
        measure()
