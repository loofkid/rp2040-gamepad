"""
Initial USB configuration tools for use in ``boot.py`` setup.

This module provides the necessary functions to create a CircuitPython USB HID device
with a descriptor that includes the configured type and quantity of inputs.
"""

try:
    from typing import Union, Literal
except ImportError:
    pass


import usb_hid  # type: ignore (this is a CircuitPython built-in
import json

from joystick_xl import __version__


def create_joystick(
    axes: int = 4,
    buttons: int = 16,
    hats: int = 1,
    triggers: int = 0,
    report_id: int = 0x04,
    gamepad: Union[False, Literal['Android'], Literal['Dinput']] = False,
) -> usb_hid.Device:
    """
    Create the ``usb_hid.Device`` required by ``usb_hid.enable()`` in ``boot.py``.

    .. note::

        JoystickXL will add an entry to the ``boot_out.txt`` file on your ``CIRCUITPY``
        drive.  It is used by the ``Joystick`` module to retrieve configuration
        settings.

    :param axes: The number of axes to support, from 0 to 8.  (Default is 4)
    :type axes: int, optional
    :param buttons: The number of buttons to support, from 0 to 128.  (Default is 16)
    :type buttons: int, optional
    :param hats: The number of hat switches to support, from 0 to 4.  (Default is 1)
    :type hats: int, optional
    :param report_id: The USB HID report ID number to use.  (Default is 4)
    :type report_d: int, optional
    :return: A ``usb_hid.Device`` object with a descriptor identifying it as a joystick
        with the specified number of buttons, axes and hat switches.
    :rtype: ``usb_hid.Device``

    """
    _num_axes = axes
    _num_buttons = buttons
    _num_hats = hats
    _num_triggers = triggers

    # Validate the number of configured axes, buttons and hats.
    if not gamepad:
        if _num_axes < 0 or _num_axes > 8:
            raise ValueError("Axis count must be from 0-8.")
    if gamepad != False:
        if _num_axes < 0 or _num_axes > 4:
            raise ValueError("Axis count must be from 0-4.")

    if _num_buttons < 0 or _num_buttons > 128:
        raise ValueError("Button count must be from 0-128.")

    if _num_hats < 0 or _num_hats > 4:
        raise ValueError("Hat count must be from 0-4.")
    
    if _num_triggers != 0 and _num_triggers != 2:
        raise ValueError("Trigger count must be 0 or 2.")

    _report_length = 0

    # Formatting is disabled below to allow the USB descriptor elements to be
    # grouped and annotated such that the descriptor is readable and maintainable.

    # fmt: off
    _descriptor = bytearray((
        0x05, 0x01,                         # : USAGE_PAGE (Generic Desktop)
        0x09, 0x05 if gamepad != False else 0x04,    # : USAGE (Joystick) or (Gamepad)
        0xA1, 0x01,                         # : COLLECTION (Application)
        0x85, report_id,                    # :   REPORT_ID (Default is 4)
    ))

    if _num_axes:
        if gamepad == "Android":
            _descriptor.extend(bytes((
                0x15, 0x00,                 # :     LOGICAL_MINIMUM (0)
                0x26, 0xFF, 0x00,           # :     LOGICAL_MAXIMUM (255)
                0x09, 0x30,                 # :     USAGE (X)
                0x09, 0x31,                 # :     USAGE (Y)
                0x09, 0x32,                 # :     USAGE (Z)
                0x09, 0x35,                 # :     USAGE (Rz)
                0x75, 0x08,                 # :     REPORT_SIZE (8)
                0x95, 0x04,                 # :     REPORT_COUNT (4)
                0x81, 0x02,                 # :     INPUT (Data,Var,Abs)
            )))
        elif gamepad == "Dinput":
            _descriptor.extend(bytes((
                0x15, 0x00,                 # :     LOGICAL_MINIMUM (0)
                0x26, 0xFF, 0x00,           # :     LOGICAL_MAXIMUM (255)
                0x09, 0x30,                 # :     USAGE (X)
                0x09, 0x31,                 # :     USAGE (Y)
                0x09, 0x33,                 # :     USAGE (Rx)
                0x09, 0x34,                 # :     USAGE (Ry)
                0x75, 0x08,                 # :     REPORT_SIZE (8)
                0x95, 0x04,                 # :     REPORT_COUNT (4)
                0x81, 0x02,                 # :     INPUT (Data,Var,Abs)
            )))
        else:
            for i in range(_num_axes):
                _descriptor.extend(bytes((
                    0x09, min(0x30 + i, 0x36)   # :     USAGE (X,Y,Z,Rx,Ry,Rz,S0,S1)
                )))
                    
            _descriptor.extend(bytes((
                0x15, 0x00,                     # :     LOGICAL_MINIMUM (0)
                0x26, 0xFF, 0x00,               # :     LOGICAL_MAXIMUM (255)
                0x75, 0x08,                     # :     REPORT_SIZE (8)
                0x95, _num_axes,                # :     REPORT_COUNT (num_axes)
                0x81, 0x02,                     # :     INPUT (Data,Var,Abs)
            )))

        _report_length = _num_axes
        
    if _num_triggers:
        print(_num_triggers)
        if gamepad == "Android":
            _descriptor.extend(bytes((
                0x05, 0x09,                     # :     USAGE_PAGE (Button)
                0x15, 0x00,                     # :     LOGICAL_MINIMUM (0)
                0x26, 0xFF, 0x00,               # :     LOGICAL_MAXIMUM (255)
                0x09, 0x06,                     # :     USAGE_MINIMUM (Button 7)
                0x09, 0x07,                     # :     USAGE_MAXIMUM (Button 8)
                0x75, 0x08,                     # :     REPORT_SIZE (8)
                0x95, 0x02,                     # :     REPORT_COUNT (num_triggers)
                0x81, 0x02,                     # :     INPUT (Data,Var,Abs)
                0x05, 0x01,                     # :     USAGE_PAGE (Generic Desktop)
            )))
            
        elif gamepad == "Dinput":
            _descriptor.extend(bytes((
                0x15, 0x00,                     # :     LOGICAL_MINIMUM (0)
                0x26, 0xFF, 0x00,               # :     LOGICAL_MAXIMUM (255)
                0x09, 0x32,                     # :     USAGE (Z)
                0x75, 0x08,                     # :     REPORT_SIZE (8)
                0x95, 0x01,                     # :     REPORT_COUNT (num_triggers)
                0x81, 0x02,                     # :     INPUT (Data,Var,Abs)
            )))
        
        _report_length += 1 if gamepad == "Dinput" else 2

    if _num_hats:
        for i in range(_num_hats):
            _descriptor.extend(bytes((
                0x09, 0x39,                 # :     USAGE (Hat switch)
            )))

        _descriptor.extend(bytes((
            0x15, 0x00,                     # :     LOGICAL_MINIMUM (0)
            0x25, 0x07,                     # :     LOGICAL_MAXIMUM (7)
            0x35, 0x00,                     # :     PHYSICAL_MINIMUM (0)
            0x46, 0x3B, 0x01,               # :     PHYSICAL_MAXIMUM (315)
            0x65, 0x14,                     # :     UNIT (Eng Rot:Angular Pos)
            0x75, 0x04,                     # :     REPORT_SIZE (4)
            0x95, _num_hats,                # :     REPORT_COUNT (num_hats)
            0x81, 0x42,                     # :     INPUT (Data,Var,Abs,Null)
        )))

        _hat_pad = _num_hats % 2
        if _hat_pad:
            _descriptor.extend(bytes((
                0x75, 0x04,                 # :     REPORT_SIZE (4)
                0x95, _hat_pad,             # :     REPORT_COUNT (_hat_pad)
                0x81, 0x03,                 # :     INPUT (Cnst,Var,Abs)
            )))

        _report_length += ((_num_hats // 2) + bool(_hat_pad))

    if _num_buttons:
        _descriptor.extend(bytes((
            0x05, 0x09,                     # :     USAGE_PAGE (Button)
        )))
        
        if gamepad == "Android":
            _descriptor.extend(bytes((
                0x09, 0x01,                     # :     USAGE (Button A)
                0x09, 0x02,                     # :     USAGE (Button B)
                0x09, 0x04,                     # :     USAGE (Button X)
                0x09, 0x05,                     # :     USAGE (Button Y)
                0x09, 0x07,                     # :     USAGE (Button L1)
                0x09, 0x08,                     # :     USAGE (Button R1)
                0x09, 0x10,                     # :     USAGE (Button Start)
                0x09, 0x11,                     # :     USAGE (Button Select)
                0x09, 0x0E,                     # :     USAGE (Button L3)
                0x09, 0x0F,                     # :     USAGE (Button R3)
                0x09, 0x0A,                     # :     USAGE (Button 1)
                0x09, 0x0B,                     # :     USAGE (Button 13)
            )))
            
            if _num_buttons > 12:
                _descriptor.extend(bytes((
                    0x19, 0x12,                     # :     USAGE_MINIMUM (Button 18)
                    0x29, 0x12 + _num_buttons - 12, # :     USAGE_MAXIMUM (num_buttons)
                )))
        else:
            _descriptor.extend(bytes((
                0x19, 0x01,                     # :     USAGE_MINIMUM (Button 1)
                0x29, _num_buttons,             # :     USAGE_MAXIMUM (num_buttons)
            )))
            
        _descriptor.extend(bytes((
            0x15, 0x00,                     # :     LOGICAL_MINIMUM (0)
            0x25, 0x01,                     # :     LOGICAL_MAXIMUM (1)
            0x95, _num_buttons,             # :     REPORT_COUNT (num_buttons)
            0x75, 0x01,                     # :     REPORT_SIZE (1)
            0x81, 0x02,                     # :     INPUT (Data,Var,Abs)
        )))      

        _button_pad = _num_buttons % 8
        if _button_pad:
            _descriptor.extend(bytes((
                0x75, 0x01,                 # :     REPORT_SIZE (1)
                0x95, 8 - _button_pad,      # :     REPORT_COUNT (_button_pad)
                0x81, 0x03,                 # :     INPUT (Cnst,Var,Abs)
            )))

        _report_length += ((_num_buttons // 8) + bool(_button_pad))

    _descriptor.extend(bytes((
        0xC0,                               # : END_COLLECTION
    )))
    # fmt: on

    # write configuration data to boot.out using 'print'
    # print(
    #     "+ Enabled JoystickXL",
    #     __version__,
    #     "with",
    #     "axes: ",
    #     _num_axes,
    #     ", buttons: ",
    #     _num_buttons,
    #     ", hats: ",
    #     _num_hats,
    #     ", and triggers: ",
    #     _num_triggers,
    #     ", for a total of ",
    #     _report_length,
    #     " report bytes.",
    # )
    mode = "joy" if not gamepad else gamepad
    
    js_config = {
        "axes": _num_axes,
        "buttons": _num_buttons,
        "hats": _num_hats,
        "triggers": _num_triggers,
        "report_length": _report_length,
        "mode": mode,
    }
    
    print("++ ", json.dumps(js_config))

    return usb_hid.Device(
        report_descriptor=bytes(_descriptor),
        usage_page=0x01,  # same as USAGE_PAGE from descriptor above
        usage=0x05 if gamepad else 0x04,  # same as USAGE from descriptor above
        report_ids=(report_id,),  # report ID defined in descriptor
        in_report_lengths=(_report_length,),  # length of reports to host
        out_report_lengths=(0,),  # length of reports from host
    )


def _get_device() -> usb_hid.Device:
    """Find a JoystickXL device in the list of active USB HID devices."""
    for device in usb_hid.devices:
        if (
            device.usage_page == 0x01
            and (device.usage == 0x04
            or device.usage == 0x05)
            and hasattr(device, "send_report")
        ):
            return device
    raise ValueError("Could not find JoystickXL HID device - check boot.py.)")
