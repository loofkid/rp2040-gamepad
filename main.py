import board
import digitalio
import analogio
import usb_hid

from gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

