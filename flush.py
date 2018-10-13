import RPi.GPIO as GPIO
import time
import logging

def flush():
    SIGNAL_PIN = 23  # GPIO_11
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(SIGNAL_PIN, GPIO.OUT)

    frequency = 50  # Hz
    msPerCycle = 1000 / frequency
    # milliseconds and duty cycle percentages for home and waive positions
    # which are at 0 and 180 degrees
    homePosition_ms = 0.5
    homePosition_dc = 100 * homePosition_ms / msPerCycle
    waivePosition_ms = 2.5
    waivePosition_dc = 100 * waivePosition_ms / msPerCycle


    def set_servo(position_dc):
        MOVE_TIME = 1
        pwm = GPIO.PWM(SIGNAL_PIN, frequency)
        pwm.start(position_dc)
        time.sleep(MOVE_TIME)
        pwm.stop()
    
    set_servo(homePosition_dc)
    set_servo(waivePosition_dc)
    time.sleep(3)
    set_servo(homePosition_dc)
    GPIO.cleanup()


if __name__ == "__main__":
    flush()
