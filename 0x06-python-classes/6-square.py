#!/usr/bin/python3
"""Define class """


class Square:
    """class """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def area(self):
        """area """
        return self.__size ** 2

    @property
    def size(self):
        """size """
        return self.__size

    @size.setter
    def size(self, value):
        """size class """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print """
        if self.__size == 0:
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("".join(["#" for j in range(self.__size)]))

    @property
    def position(self):
        """pos """
        return self.__position

    @position.setter
    def position(self, value):
        """pos class """
        if type(value[1]) == int and value[1] >= 0 and\
                type(value[0]) == int and value[0] >= 0 and\
                len(value) == 2 and type(value) == tuple:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
