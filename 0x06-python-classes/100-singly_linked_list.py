#!/usr/bin/python3
class Node():

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

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
    @data.setter
    def next_node(self, value):
        if self.__next_node == None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value 


class SinglyLinkedList():
    def __init__(self):
        self.__head = None 
    def printlist(self):
        temp = self.__head
        while(temp):
            print(temp.data)
            temp = next_node(temp.next)
    def __repr__(self):
        return(self.printlist())
    def sorted_insert(self, value):
        new = Node(value)
        if self.__head == None:
            self.__head = new
        else:
            new.next = self.__head
            self.__head = new
