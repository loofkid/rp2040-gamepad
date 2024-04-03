import board
from joystick_xl.joystick import Joystick
from multiplexer import Multiplexer
from button_matrix import ButtonMatrix

multiplexer = Multiplexer()
button_matrix = ButtonMatrix()

joystick = Joystick()

joystick.add_input(
    multiplexer.LX,
    multiplexer.LY,
    multiplexer.RX,
    multiplexer.RY,
    multiplexer.TL,
    multiplexer.TR,
    button_matrix.Hat,
    button_matrix.B1,
    button_matrix.B2,
    button_matrix.B3,
    button_matrix.B4,
    button_matrix.B5,
    button_matrix.B6,
    button_matrix.B7,
    button_matrix.B8,
    button_matrix.B9,
    button_matrix.B10,
    button_matrix.B13,
    button_matrix.B14,
    button_matrix.B15,
    button_matrix.B16,
    button_matrix.B17,
    button_matrix.B18,
)

while True:
    joystick.update()