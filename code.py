import time
import board
import digitalio
import analogio
import usb_hid

from gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

button = False

while True:
    if button:
        gp.press_button(1)
    else:
        gp.release_button(1)
    button = not button
    gp.move_joysticks(0, 0)
    gp.move_triggers(0, 0)
    time.sleep(0.1)