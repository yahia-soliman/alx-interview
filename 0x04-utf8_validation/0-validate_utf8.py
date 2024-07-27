#!/usr/bin/python3
"""UTF-8 Validation

Given a stream of bytes in an array:
    validate if it represent a valid UTF-8 encoding
"""


def validUTF8(data):
    """Validate a stream of bytes according to UTF-8 encoding
    """
    sub_bytes = 0
    for b in data:
        idx_0 = idx_of_0(b)
        if (sub_bytes > 0 and idx_0 != 1) or idx_0 > 4:
            return False
        if idx_0 != 1:
            sub_bytes = idx_0
        sub_bytes -= 1
    return sub_bytes <= 0


def idx_of_0(number):
    """Calculate how long a utf char in bytes
    """
    b = 0b10000000
    i = 0
    while number & b:
        i += 1
        b >>= 1
    return i
