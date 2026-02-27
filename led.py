import RPi.GPIO as GPIO
from time import sleep
import random

# Initial Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Define 7 LED pins (Physical Pins)
leds = [29, 31, 33, 35, 37, 36, 38]

# Set all pins as output and turn them off
for pin in leds:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def disco_random():
    """Flashes random LEDs at high speed"""
    for _ in range(20):
        # Pick a random number of LEDs to turn on (1 to 7)
        num_on = random.randint(1, 7)
        # Randomly choose which LEDs those are
        active_leds = random.sample(leds, num_on)
       
        # Turn on selected LEDs
        for pin in leds:
            GPIO.output(pin, GPIO.HIGH if pin in active_leds else GPIO.LOW)
       
        sleep(0.1) # Fast flash

def disco_chase():
    """Quick back-and-forth 'Knight Rider' style"""
    for _ in range(3):
        for pin in leds:
            GPIO.output(pin, GPIO.HIGH)
            sleep(0.05)
            GPIO.output(pin, GPIO.LOW)
        for pin in reversed(leds):
            GPIO.output(pin, GPIO.HIGH)
            sleep(0.05)
            GPIO.output(pin, GPIO.LOW)

try:
    print("Disco mode active! Press Ctrl+C to stop.")
    while True:
        # Switch between different 'dance' modes
        disco_random()
        disco_chase()

except KeyboardInterrupt:
    print("\nEnding the party...")

finally:
    # Cleanup: Turn everything off safely
    for pin in leds:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
