from pyfirmata2 import Arduino, util
import time

board = Arduino('COM9')

pins = [8,9,10,11,12]

print("Testing LEDs...")

for i in pins:
    board.digital[i].write(1)
    print(f"LED on pin {i} ON")
    time.sleep(1)
    board.digital[i].write(0)
    print(f"LED on pin {i} OFF")
