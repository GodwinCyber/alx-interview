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
    count_bytes = 0

    num_UTF8_1 = 1 << 7
    num_UTF8_2 = 1 << 6

    for byte in data:

        mask_byte = 1 << 7

        if count_bytes == 0:

            while mask_byte & byte:
                count_bytes += 1
                mask_byte = mask_byte >> 1

            if count_bytes == 0:
                continue

            if count_bytes == 1 or count_bytes > 4:
                return False

        else:
            if not (byte & num_UTF8_1 and not (byte & num_UTF8_2)):
                return False

        count_bytes -= 1

    if count_bytes == 0:
        return True

    return False
