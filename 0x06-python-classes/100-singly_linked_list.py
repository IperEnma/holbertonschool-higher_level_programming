#!/usr/bin/python3
class Node():

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if value != None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value 


class SinglyLinkedList():
    def __init__(self):
        self.__head = None 

    def sorted_insert(self, value):
        current = self.__head
        new = Node(value)
        if current == None:
            self.__head = new
        elif current.data >= new.data:
            new.next_node = self.__head
            self.__head = new
        else:
            new = Node(value)
            while current.next_node and current.next_node.data < new.data:
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        string = ""
        current = self.__head
        while current:
            string = string + str(current.data)
            if current.next_node:
                    string = string + "\n"
            current = current.next_node
        return string
