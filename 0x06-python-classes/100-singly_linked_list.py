#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data)
            string += "\n"
            tmp = tmp.next_node
        string = string[:-1]
        return string

    def sorted_insert(self, value):
        node = Node(value)
        tmp = self.__head
        if tmp:
            node.next_node = tmp
        if tmp is None or tmp.data >= value:
            self.__head = node
            return
        while tmp.next_node is not None and tmp.data < value:
            if tmp.next_node.data >= value:
                break
            tmp = tmp.next_node
        node.next_node = tmp.next_node
        tmp.next_node = node
