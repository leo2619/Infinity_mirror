##button_init.py
#initialization and processing of signal sent by button

import RPi.GPIO as GPIO

class Button:
    def __init__(self, pin, callback=None, bouncetime=300):
        self.pin = pin
        self.callback = callback

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, GPIO.FALLING, callback=self._internal_callback, bouncetime=bouncetime)

    def _internal_callback(self):
        if self.callback is not None:
            self.callback()

    def cleanup(self):
        GPIO.cleanup(self.pin)