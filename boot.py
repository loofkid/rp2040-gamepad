import usb_hid
from joystick_xl.hid import create_joystick
import supervisor

supervisor.set_usb_identification("Loof Home Automations", "Crackbone Gamepad", 0x1209, 0x6660)

usb_hid.disable()

usb_hid.enable((
    create_joystick(axes=6, buttons=16, hats=1),
))