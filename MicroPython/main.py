"""
Created by: Michael B
Created on: Sep 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *

# setup
display.clear()
pin16.write_digital(0)
display.show(Image.Happy)

# turn on LED
while True:
    if button_a.is_pressed():
        pin16.write_digital(1)
        display.show(Image.Yes)

while True:
    if button_a.is_pressed():
        pin16.write_digital(0)
        display.show(Image.No)
