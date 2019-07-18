from enum import Enum


class Color(Enum):
    red = [0xFF, 0x00, 0x00]
    green = [0x00, 0xFF, 0x00]
    blue = [0x00, 0x00, 0xFF]
    off = [0x00, 0x00, 0x00]
    white = [0xFF, 0xFF, 0xFF]
    yellow = [0xFF, 0x90, 0x00]
    purple = [0xFF, 0x00, 0xFF]
    orange = [0xFF, 0x20, 0x00]
    pink = [0xFF, 0x66, 0xB2]
