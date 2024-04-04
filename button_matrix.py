import adafruit_matrixkeypad
from digitalio import DigitalInOut, Direction, Pull
import board
from joystick_xl.inputs import Button, Hat

class ButtonMatrix:

    ''' 
        Gamepad Layout:
        
        Front:
           _____________________________________    
         /         |                    |        \`
        /  5       |                    |     6    \`
        |------------                    ------------|
        |                                      4     |
        |    9                              3     2  |
        |                                      1     |
        |                                            |      
        |   H1                                       |
        |H4    H2                              10    |
        |   H3                                       |
        |                                            |   
        | 7    13                           14    8  |
        \___________________________________________/
        
        Back:
        
            15                                 16
            
            17                                 18
    '''

    buttons = ((1, 2, 3, 4),
            (5, 6, 9, 10),
            ("H1", "H2", "H3", "H4"),
            (7, 8, 13, 14),
            (15, 16, 17, 18))
    
    def __init__(self):
        self.cols = [DigitalInOut(x) for x in (board.D2, board.D3, board.D4, board.D5)]
        self.rows = [DigitalInOut(x) for x in (board.D6, board.D7, board.D8, board.D9, board.D10)]
        self.keypad = adafruit_matrixkeypad.Matrix_Keypad(self.rows, self.cols, self.buttons)
    
    @staticmethod    
    def _validate_button(self, button):
        flat_buttons = [item for sublist in self.buttons for item in sublist]
        if button not in flat_buttons:
            raise ValueError("Invalid button number")
        return button
        
    def _get_button_state(self, button):
        if ButtonMatrix._validate_button(button):
           return button in self.keypad.pressed_keys
        return False
    
    def _get_xl_button(self, button):
        return Button(self._get_button_state(button))
    
    @property
    def B1(self):
        return self._get_xl_button(1)
    
    @property
    def B2(self):
        return self._get_xl_button(2)
    
    @property
    def B3(self):
        return self._get_xl_button(3)
    
    @property
    def B4(self):
        return self._get_xl_button(4)
    
    @property
    def B5(self):
        return self._get_xl_button(5)
    
    @property
    def B6(self):
        return self._get_xl_button(6)
    
    @property
    def B7(self):
        return self._get_xl_button(7)
    
    @property
    def B8(self):
        return self._get_xl_button(8)
    
    @property
    def B9(self):
        return self._get_xl_button(9)
    
    @property
    def B10(self):
        return self._get_xl_button(10)
    
    @property
    def B13(self):
        return self._get_xl_button(13)
    
    @property
    def B14(self):
        return self._get_xl_button(14)
    
    @property
    def B15(self):
        return self._get_xl_button(15)
    
    @property
    def B16(self):
        return self._get_xl_button(16)
    
    @property
    def B17(self):
        return self._get_xl_button(17)
    
    @property
    def B18(self):
        return self._get_xl_button(18)
    
    @property
    def Hat(self):
        return Hat(
            up=self._get_button_state("H1"),
            right=self._get_button_state("H2"),
            down=self._get_button_state("H3"),
            left=self._get_button_state("H4")
        )
    
class ButtonInput:
    def __init__(self, button, value=False):
        self.button = button
        self.value = value