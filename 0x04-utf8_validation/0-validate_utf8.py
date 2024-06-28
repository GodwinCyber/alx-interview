#!/usr/bin/python3
"""Module UTF-8 Validation"""


def validUTF8(data):
    """A method that determines if a given data set represents a
        valid UTF-8 encoding. Prototype: def validUTF8(data)
        Return: True if data is a valid UTF-8 encoding, else
        return False A character in UTF-8 can be 1 to 4 bytes long
        The data set can contain multiple characters
        The data will be represented by a list of integers
        Each integer represents 1 byte of data, therefore you only need to
        handle the 8 least significant bits of each integer
    """
    count_byte = 0

    num_UTF8_1 = 1 << 7
    num_UTF8_2 = 1 << 6

    for byte in data:
        num_byte = 1 << 7

        if count_byte == 0:
            while num_byte & byte:
                count_byte += 1
                num_byte = count_byte >> 1

            if count_byte == 0:
                continue
            if count_byte == 1 or count_byte > 4:
                return False
        else:
            if not (byte & num_UTF8_1 and not (byte & num_UTF8_2)):
                return False
        count_byte -= 1
    if count_byte == 0:
        return True
    else:
        return False
