#!/usr/bin/python3
"""A simple module that defines a class square"""


class Square:

    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.
        Args:
            size(int): Private attribute for size of square.
            position: Private attribute for position
        Return:
            None
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter function to retrieve size attribute.
        Return:
            size of obj.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function to validate size
        Args:
            value(int): int object
        """

        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value >= 0:
            self.__size = value
        else:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Getter function to retrieve private position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter function to validate position
        Args:
            value(int): int object
        """

        if not isinstance(value, tuple) or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value[:]

    def area(self):
        """Public instance area method
            Args:
                self: object
            Return:
                current square area
        """
        return self.__size ** 2

    def my_print(self):
        """Function that prints in stdout square with char #"""
        if self.__size == 0:
            print()
            return


        copy = self.__position[:]
        print("{}".format('\n' * copy[1]), end="")

        for x in range(self.__size):
            print("{}{}".format(' ' * copy[0], '#' * self.__size))
