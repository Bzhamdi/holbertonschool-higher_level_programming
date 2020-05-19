#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
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
        return self.__position

    @position.setter
    def position(self, value):
        if type(value[1]) == int and value[1] >= 0 and\
                type(value[0]) == int and value[0] >= 0 and\
                len(value) == 2 and type(value) == tuple:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
