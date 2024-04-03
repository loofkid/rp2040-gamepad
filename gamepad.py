import struct
import time

from adafruit_hid import find_device

class Gamepad:
    def __init__(self, devices):
        self._gamepad_device = find_device(devices, usage_page=0x01, usage=0x05)
        
        
        # Reuse this byetearray to send reports.
        # Typically controllers start numbering buttons at 1 rather than 0.
        # report[0] buttons 1-8 (LSB is button 1)
        # report[1] buttons 9-16
        # report[2] buttons 17-24
        # report[3] joystick 0 x (-127 to 127)
        # report[4] joystick 0 y (-127 to 127)
        # report[5] joystick 1 x (-127 to 127)
        # report[6] joystick 1 y (-127 to 127)
        # report[7] trigger L (0 to 255)
        # report[8] trigger R (0 to 255)
        self._report = bytearray(7)
        
        # Keep track of the last report sent to avoid sending duplicate reports.
        self._last_report = bytearray(7)
        
        # Initialize the report with the default values.
        self._buttons_state = 0
        self._joy_x = 0
        self._joy_y = 0
        self._joy_z = 0
        self._joy_rx = 0
        self._joy_ry = 0
        self._joy_rz = 0
        
        
    def press_buttons(self, *buttons):
        for button in buttons:
            self._buttons_state |= 1 << self._validate_button_number(button) - 1
        self._send()
        
    def release_buttons(self, *buttons):
        for button in buttons:
            self._buttons_state &= ~(1 << self._validate_button_number(button) - 1)
        self._send()
        
    def release_all_buttons(self):
        self._buttons_state = 0
        self._send()
        
    def click_buttons(self, *buttons):
        self.press_buttons(*buttons)
        self.release_buttons(*buttons)
        
    def move_joysticks(self, x=None, y=None, z=None, rx=None):
        if x is not None:
            self._joy_x = self._validate_joystick_value(x)
        if y is not None:
            self._joy_y = self._validate_joystick_value(y)
        if z is not None:
            self._joy_z = self._validate_joystick_value(z)
        if rx is not None:
            self._joy_rx = self._validate_joystick_value(rx)
        self._send()
        
    def move_triggers(self, l=None, r=None):
        if l is not None:
            self._joy_ry = self._validate_trigger_value(l)
        if r is not None:
            self._joy_rz = self._validate_trigger_value(r)
        self._send()
    
    def reset_all(self):
        self._buttons_state = 0
        self._joy_x = 0
        self._joy_y = 0
        self._joy_z = 0
        self._joy_rx = 0
        self._joy_ry = 0
        self._joy_rz = 0
        self._send(always=True)
        
    def _send(self, always=False):
        struct.pack_into(
            "<Hbbbbbb",
            self._report,
            0,
            self._buttons_state,
            self._joy_x,
            self._joy_y,
            self._joy_z,
            self._joy_rx,
            self._joy_ry,
            self._joy_rz
        )
        
        if always or self._last_report != self._report:
            self._gamepad_device.send_report(self._report)
            # Remember what we sent, without allocating new storage.
            self._last_report[:] = self._report
        
    @staticmethod
    def _validate_button_number(button: int):
        if not 1 <= button <= 20:
            raise ValueError("Button number must in range 1 to 20")
        return button

    @staticmethod
    def _validate_joystick_value(value: int):
        if not -127 <= value <= 127:
            raise ValueError("Joystick value must be in range -127 to 127")
        return value
    
    @staticmethod
    def _validate_trigger_value(value: int):
        if not 0 <= value <= 255:
            raise ValueError("Trigger value must be in range 0 to 255")
        return value
    
    @staticmethod
    def _range_map(x: int, in_min: int, in_max: int, out_min: int, out_max: int):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    @staticmethod
    def normalize_joystick_value(value: int):
        return Gamepad._range_map(value, 0, 4096, -127, 127)
    
    @staticmethod
    def normalize_trigger_value(value: int):
        return Gamepad._range_map(value, 0, 4096, 0, 255)