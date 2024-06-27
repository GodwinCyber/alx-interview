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

    for num in data:
        if count == 0:
            if (num >> 5) == 0b110:
                count = 1
            elif (num >> 4) == 0b1110:
                count = 2
            elif (num >> 3) == 0b11110:
                count = 3
            elif (num >> 7):
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            count -= 1
    return count == 0
