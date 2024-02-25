import RPi.GPIO as GPIO
import time
import subprocess as sp
import math

Fan = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Fan, GPIO.OUT)

p = GPIO.PWM(Fan, 50)
p.start(0)

try:
    while True:

        temp = sp.getoutput("vcgencmd measure_temp|egrep -o '[0-9]*\.[0-9]*'")
        if float(temp) < 40:
            p.ChangeDutyCycle(0)
        elif float(temp) > 70.0:
            p.ChangeDutyCycle(100)
        else:
            step = 80 / 30
            delta = float(temp) - 40
            speed = 20 + (round(delta) * step)
            p.ChangeDutyCycle(speed)

        time.sleep(0.1)


except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
