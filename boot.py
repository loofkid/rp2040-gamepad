# 

import usb_hid
from joystick_xl.hid import create_joystick

usb_hid.enable((
    create_joystick(axes=6, buttons=16, hats=4),
))