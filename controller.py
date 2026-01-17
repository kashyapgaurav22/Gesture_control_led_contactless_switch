from pyfirmata2 import Arduino

PORT = Arduino.AUTODETECT
board = Arduino(PORT)

# Use the same pins as test.py (8–12)
led_1 = board.get_pin('d:8:o')   # Thumb
led_2 = board.get_pin('d:9:o')   # Index
led_3 = board.get_pin('d:10:o')  # Middle
led_4 = board.get_pin('d:11:o')  # Ring
led_5 = board.get_pin('d:12:o')  # Pinky

def led(fingerUp):
    thumb, index, middle, ring, pinky = fingerUp

    # Reset all LEDs first
    for led in [led_1, led_2, led_3, led_4, led_5]:
        led.write(0)

    # Map each finger to one LED
    if thumb:
        led_1.write(1)
    if index:
        led_2.write(1)
    if middle:
        led_3.write(1)
    if ring:
        led_4.write(1)
    if pinky:
        led_5.write(1)

