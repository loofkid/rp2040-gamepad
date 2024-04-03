import time
from typing import Optional

import board
import digitalio
from microcontroller import Pin
from supervisor import runtime

from joystick_xl.joystick import Joystick

def TestAxes(js: Joystick, step: int = 5, quiet: bool = False) -> None: ...
def TestButtons(js: Joystick, pace: float = 0.05, quiet: bool = False) -> None: ...
def TestHats(js: Joystick, pace: float = 0.25, quiet: bool = False) -> None: ...
def TestConsole(button_pin: Optional[Pin] = None) -> None: ...
