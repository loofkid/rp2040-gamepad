import usb_hid

GAMEPAD_REPORT_DESCRIPTOR = bytes((
    0x05, 0x01,                    # USAGE_PAGE (Generic Desktop)
    0x09, 0x05,                    # USAGE (Game Pad)
    0xa1, 0x01,                    # COLLECTION (Application)
    0x85, 0x04,                    #   REPORT_ID (4)
    0x05, 0x09,                    #   USAGE_PAGE (Button)
    0x19, 0x01,                    #   USAGE_MINIMUM (Button 1)
    0x29, 0x14,                    #   USAGE_MAXIMUM (Button 20)
    0x15, 0x00,                    #   LOGICAL_MINIMUM (0)
    0x25, 0x01,                    #   LOGICAL_MAXIMUM (1)
    0x95, 0x14,                    #   REPORT_COUNT (20)
    0x75, 0x01,                    #   REPORT_SIZE (1)
    0x81, 0x02,                    #   INPUT (Data,Var,Abs)
    0x15, 0x00,                    #   LOGICAL_MINIMUM (0)
    0x25, 0x07,                    #   LOGICAL_MAXIMUM (7)
    0x35, 0x00,                    #   PHYSICAL_MINIMUM (0)
    0x46, 0xFF, 0x00,              #   PHYSICAL_MAXIMUM (255)
    0x65, 0x14,                    #   UNIT (System: English Rotation, Length: Centimeter)
    0x09, 0x39,                    #   USAGE (Hat switch)
    0x81, 0x42,                    #   INPUT (Data,Var,Abs,Null)
    0x65, 0x00,                    #   UNIT (None)
    0x05, 0x01,                    #   USAGE_PAGE (Generic Desktop)
    0x09, 0x01,                    #   USAGE (Pointer)
    0xa1, 0x00,                    #   COLLECTION (Physical)
    0x09, 0x30,                    #     USAGE (X)
    0x09, 0x31,                    #     USAGE (Y)
    0x95, 0x02,                    #     REPORT_COUNT (2)
    0x75, 0x08,                    #     REPORT_SIZE (8)
    0x15, 0x81,                    #     LOGICAL_MINIMUM (-127)
    0x25, 0x7F,                    #     LOGICAL_MAXIMUM (127)
    0x35, 0x81,                    #     PHYSICAL_MINIMUM (-127)
    0x45, 0x7F,                    #     PHYSICAL_MAXIMUM (127)
    0x81, 0x02,                    #     INPUT (Data,Var,Abs)
    0xc0,                          #   END_COLLECTION
    0x09, 0x32,                    #   USAGE (Z)
    0x09, 0x35,                    #   USAGE (Rz)
    0x95, 0x02,                    #   REPORT_COUNT (2)
    0x75, 0x08,                    #   REPORT_SIZE (8)
    0x15, 0x00,                    #   LOGICAL_MINIMUM (0)
    0x25, 0xFF,                    #   LOGICAL_MAXIMUM (255)
    0x35, 0x00,                    #   PHYSICAL_MINIMUM (0)
    0x46, 0xFF, 0x00,              #   PHYSICAL_MAXIMUM (255)
    0x81, 0x02,                    #   INPUT (Data,Var,Abs)
    0x05, 0x09,                    #   USAGE_PAGE (Button)
    0x19, 0x15,                    #   USAGE_MINIMUM (Button 21)
    0x29, 0x16,                    #   USAGE_MAXIMUM (Button 22)
    0x15, 0x00,                    #   LOGICAL_MINIMUM (0)
    0x25, 0x01,                    #   LOGICAL_MAXIMUM (1)
    0x95, 0x02,                    #   REPORT_COUNT (2)
    0x75, 0x01,                    #   REPORT_SIZE (1)
    0x81, 0x02,                    #   INPUT (Data,Var,Abs)
    0xc0,                           # END_COLLECTION
))

gamepad = usb_hid.Device(
    report_descriptor=GAMEPAD_REPORT_DESCRIPTOR,
    usage_page=0x01,
    usage=0x05,
    report_ids=(4,),
    in_report_lengths=(9,),
    out_report_lengths=(0,)
)

usb_hid.enable((
    usb_hid.Device.KEYBOARD,
    usb_hid.Device.MOUSE,
    usb_hid.Device.CONSUMER_CONTROL,
    gamepad
))