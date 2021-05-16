import RPi.GPIO as GPIO
import time
import logging

# Settings
frequency = 50  # Hz
ms_per_cycle = 1000 / frequency
degrees_0 = 0.5  # min degrees
degrees_180 = 2.5  # max degrees
SIGNAL_PIN = 23  # GPIO_11

def init_gpio():
    # Initialization
    GPIO.setmode(GPIO.BOARD)

def shutdown_gpio():
    GPIO.cleanup()

# Helper
def set_servo(degrees):
    MOVE_TIME = 1
    # compute the duty cycle percentage for angle==degrees
    if not 0 <= degrees <= 180:
        logging.warning(
            "Cannot set servo angle to {}. Valid angles in [0, 180]"
            .format(degrees)
        )
        return
    degrees_ms = degrees_0 + (degrees_180 - degrees_0) / 180 * degrees
    degrees_dc = 100 * degrees_ms / ms_per_cycle
    pwm = GPIO.PWM(SIGNAL_PIN, frequency)
    pwm.start(degrees_dc)
    time.sleep(MOVE_TIME)
    pwm.stop()

def flush():
    # Waive
    home_angle = 170
    waive_angle = 10
    GPIO.setup(SIGNAL_PIN, GPIO.OUT)

    set_servo(home_angle)
    set_servo(waive_angle)
    time.sleep(3)
    set_servo(home_angle)


if __name__ == "__main__":
    init_gpio()

    try:
        flush()

    finally:
        shutdown_gpio()

