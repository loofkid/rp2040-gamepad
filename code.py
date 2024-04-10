import board
from gamepad_xl.gamepad import Joystick
from gamepad_xl.inputs import Button, Hat, Axis, Trigger
from multiplexer import Multiplexer
from button_matrix import ButtonMatrix

multiplexer = Multiplexer()
button_matrix = ButtonMatrix()

joystick = Joystick()

joystick.add_input(
    Axis(),
    Axis(),
    Axis(),
    Axis(),
    Trigger(),
    Trigger(),
    Hat(),
    Button(),
    Button(),
    Button(),
    Button(),
    Button(),
    Button(),
    Button(),
    Button(),
    Button(),
    Button(),
    Button(),
    Button(),
    Button(),
    Button(),
    Button(),
    Button()
)

while True:
    LX = multiplexer.LX
    LY = multiplexer.LY
    RX = multiplexer.RX
    RY = multiplexer.RY
    TL = multiplexer.TL
    TR = multiplexer.TR
    H1 = button_matrix.H1
    H2 = button_matrix.H2
    H3 = button_matrix.H3
    H4 = button_matrix.H4
    B1 = button_matrix.B1
    B2 = button_matrix.B2
    B3 = button_matrix.B3
    B4 = button_matrix.B4
    B5 = button_matrix.B5
    B6 = button_matrix.B6
    B7 = button_matrix.B7
    B8 = button_matrix.B8
    B9 = button_matrix.B9
    B10 = button_matrix.B10
    B13 = button_matrix.B13
    B14 = button_matrix.B14
    B15 = button_matrix.B15
    B16 = button_matrix.B16
    B17 = button_matrix.B17
    B18 = button_matrix.B18
    
    joystick.axis[0].source_value = LX.value
    joystick.axis[1].source_value = LY.value
    joystick.axis[2].source_value = RX.value
    joystick.axis[5].source_value = RY.value
    joystick.trigger[0].source_value = TR.value
    joystick.trigger[1].source_value = TL.value
    joystick.hat[0].up.source_value = H1.value
    joystick.hat[0].right.source_value = H2.value
    joystick.hat[0].down.source_value = H3.value
    joystick.hat[0].left.source_value = H4.value
    joystick.button[0].source_value = B1.value
    joystick.button[1].source_value = B2.value
    joystick.button[2].source_value = B3.value
    joystick.button[3].source_value = B4.value
    joystick.button[4].source_value = B5.value
    joystick.button[5].source_value = B6.value
    joystick.button[6].source_value = B7.value
    joystick.button[7].source_value = B8.value
    joystick.button[8].source_value = B9.value
    joystick.button[9].source_value = B10.value
    joystick.button[10].source_value = B13.value
    joystick.button[11].source_value = B14.value
    joystick.button[12].source_value = B15.value
    joystick.button[13].source_value = B16.value
    joystick.button[14].source_value = B17.value
    joystick.button[15].source_value = B18.value
    
    joystick.update(True)