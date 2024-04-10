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
    
    def __init__(self, 
                 cols = [board.GP0, board.GP1, board.GP2, board.GP3,], 
                 rows = [board.GP4, board.GP5, board.GP6, board.GP7, board.GP8],
                 buttons = ((1, 2, 3, 4),
                            (6, 10, 14, 8),
                            ("H1", "H2", "H3", "H4"),
                            (5, 9, 7, 13),
                            (15, 16, 17, 18))):
        self.cols = [DigitalInOut(col) for col in cols]
        self.rows = [DigitalInOut(row) for row in rows]
        self.buttons = buttons
        self.keypad = adafruit_matrixkeypad.Matrix_Keypad(self.rows, self.cols, self.buttons)
      
    def _validate_button(self, button):
        flat_buttons = [item for sublist in self.buttons for item in sublist]
        if button not in flat_buttons:
            raise ValueError("Invalid button number")
        return button
        
    def _get_button_state(self, button):
        if self._validate_button(button):
           return button in self.keypad.pressed_keys
        return False
    
    def _get_button(self, button):
        return ButtonInput(button, not self._get_button_state(button))
    
    @property
    def B1(self):
        return self._get_button(1)
    
    @property
    def B2(self):
        return self._get_button(2)
    
    @property
    def B3(self):
        return self._get_button(3)
    
    @property
    def B4(self):
        return self._get_button(4)
    
    @property
    def B5(self):
        return self._get_button(5)
    
    @property
    def B6(self):
        return self._get_button(6)
    
    @property
    def B7(self):
        return self._get_button(7)
    
    @property
    def B8(self):
        return self._get_button(8)
    
    @property
    def B9(self):
        return self._get_button(9)
    
    @property
    def B10(self):
        return self._get_button(10)
    
    @property
    def B13(self):
        return self._get_button(13)
    
    @property
    def B14(self):
        return self._get_button(14)
    
    @property
    def B15(self):
        return self._get_button(15)
    
    @property
    def B16(self):
        return self._get_button(16)
    
    @property
    def B17(self):
        return self._get_button(17)
    
    @property
    def B18(self):
        return self._get_button(18)
    
    @property
    def H1(self):
        return self._get_button("H1")
    
    @property
    def H2(self):
        return self._get_button("H2")
    
    @property
    def H3(self):
        return self._get_button("H3")
    
    @property
    def H4(self):
        return self._get_button("H4")
    
class ButtonInput:
    def __init__(self, button, value=False):
        self.button = button
        self.value = value