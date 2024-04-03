import usb_hid

GAMEPAD_REPORT_DESCRIPTOR = bytes((
    0x05, 0x01,  # Usage Page (Generic Desktop)
    0x09, 0x05,  # Usage (Game Pad)
    0xA1, 0x01,  # Collection (Application)
    0x85, 0x08,  #   Report ID (4)
    
    # Joysticks
    0x05, 0x01,  # Usage Page (Generic Desktop)
    0x09, 0x01,  # Usage (Pointer)
    0xA1, 0x00,  # Collection (Physical)
    0x15, 0x81,  # Logical Minimum (-127)
    0x25, 0x7F,  # Logical Maximum (127)
    0x75, 0x08,  # Report Size (8 bits)
    0x95, 0x02,  # Report Count (2)
    0x05, 0x01,  # Usage Page (Generic Desktop)
    0x09, 0x30,  # Usage (X)
    0x09, 0x31,  # Usage (Y)
    0x81, 0x02,  # Input (Data, Variable, Absolute)
    0xC0,        # End Collection
    
    # Buttons
    0x05, 0x09,  # Usage Page (Button)
    0x19, 0x01,  # Usage Minimum (Button 1)
    0x29, 0x14,  # Usage Maximum (Button 20)
    0x15, 0x00,  # Logical Minimum (0)
    0x25, 0x01,  # Logical Maximum (1)
    0x75, 0x01,  # Report Size (1 bit)
    0x95, 0x14,  # Report Count (20 bits)
    0x81, 0x02,  # Input (Data, Variable, Absolute)
    
    # Triggers
    0x05, 0x01,  # Usage Page (Generic Desktop)
    0x09, 0x33,  # Usage (Rx)
    0x09, 0x34,  # Usage (Ry)
    0x15, 0x00,  # Logical Minimum (0)
    0x25, 0xFF,  # Logical Maximum (255)
    0x75, 0x08,  # Report Size (8 bits)
    0x95, 0x02,  # Report Count (2)
    0x81, 0x02,  # Input (Data, Variable, Absolute)
    
    0xC0,        # End Collection
))

print ("ugh")

gamepad = usb_hid.Device(
    report_descriptor=GAMEPAD_REPORT_DESCRIPTOR,
    usage_page=0x01,
    usage=0x05,
    report_ids=(8,),
    in_report_lengths=(7,),
    out_report_lengths=(0,)
)

print("toot")

usb_hid.enable((
    usb_hid.Device.KEYBOARD,
    usb_hid.Device.MOUSE,
    usb_hid.Device.CONSUMER_CONTROL,
    gamepad
))

print("fart")