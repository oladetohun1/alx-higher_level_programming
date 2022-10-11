#!/usr/bin/python3
"""Module containing the square class"""


class Square:
    """Square class with private attribute"""

    def __init__(self, size=0):
        """ Initialize sqaure

        Args:
            size (int): size of the square
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ calculate the area

        Returns:
            area
        """

        return self.__size * self.__size
