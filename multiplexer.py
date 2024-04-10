from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
from board import A0, GP11, GP12, GP13, GP15
from gamepad_xl.inputs import Axis
from time import sleep

class Multiplexer:
    '''
                        s0 s1 s2
        X-Axis L (LX):   0  0  0
        Y-Axis L (LY):   1  0  0
        X-Axis R (RX):   0  1  0
        Y-Axis R (RY):   1  1  0
        Trigger L (TL):  0  0  1
        Trigger R (TY):  1  0  1 
        
        s3 is tied to ground
    '''
    
    def __init__(self, adc = A0, s0 = GP11, s1 = GP12, s2 = GP13, e = GP15):
        
        self.adc = AnalogIn(adc)
        self.s0 = DigitalInOut(s0)
        self.s1 = DigitalInOut(s1)
        self.s2 = DigitalInOut(s2)
        self.e = DigitalInOut(e)
        self.s0.direction = Direction.OUTPUT
        self.s1.direction = Direction.OUTPUT
        self.s2.direction = Direction.OUTPUT
        self.e.direction = Direction.OUTPUT
        self.s0.value = False
        self.s1.value = False
        self.s2.value = False
        self.e.value = True
        
    axis_dict = {
        "LX": (0, 0, 0),
        "LY": (1, 0, 0),
        "RX": (0, 1, 0),
        "RY": (1, 1, 0),
        "TL": (0, 0, 1),
        "TR": (1, 0, 1)
    }
        
    def _validate_axis(self, axis: str):
        if axis not in ("LX", "LY", "RX", "RY", "TL", "TR"):
            raise ValueError("Invalid axis")
        return axis
    
    def _get_value(self, axis: str):
        axis = self._validate_axis(axis)
        self.e.value = False
        self.s0.value, self.s1.value, self.s2.value = self.axis_dict[axis]
        
        print(f'reading {axis}. s0: {self.s0.value}, s1: {self.s1.value}, s2: {self.s2.value}')
        
        adc_value = self.adc.value
        print(f'{axis} value: {adc_value}')
        self.e.value = True
        return adc_value
    
    def _get_mp_axis(self, axis: str):
        return MPAxis(axis, self._get_value(axis))
    
    @property
    def LX(self):
        return self._get_mp_axis("LX")
    
    @property
    def LY(self):
        return self._get_mp_axis("LY")
    
    @property
    def RX(self):
        return self._get_mp_axis("RX")
    
    @property
    def RY(self):
        return self._get_mp_axis("RY")
    
    @property
    def TL(self):
        return self._get_mp_axis("TL")
    
    @property
    def TR(self):
        return self._get_mp_axis("TR")
        
        
class MPAxis:
    def __init__(self, axis: str, value = 0):
        self.axis = axis
        self.value = value