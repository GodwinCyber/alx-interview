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
    count = 0

    num_1 = 1 << 7
    num_2 = 1 << 6

    for i in data:
        num_byte = 1 << 7

        if count == 0:
            while num_byte & i:
                count += 1
                num_byte = count >> 1

            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
        else:
            if not (i & num_1 and not (i & num_2)):
                return False
        count -= 1
    return count == 0
