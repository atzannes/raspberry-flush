import RPi.GPIO as GPIO
import time
import logging
from .flush import flush


def init_gpio():
    GPIO.setmode(GPIO.BOARD)

def shutdown_gpio():
    GPIO.cleanup()

def watch_button_push(signal_pin=16):
    GPIO.setup(signal_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    try:
        while True:
            val = GPIO.input(signal_pin)
            if val == 1:
                logging.info("Button Pressed")
                flush()

            time.sleep(0.1)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    init_gpio()

    try:
        watch_button_push()

    finally:
        shutdown_gpio()
