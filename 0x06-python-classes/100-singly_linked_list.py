#!/usr/bin/python3
"""A simple module that defines a class Node"""


class Node:

    """defines Node class"""
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
        self.__data = value

    @property
        def next_node(self):
            return self.__next_node
        
    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None: 
            raise TypeError("next_node must be a Node object")
            self.__next_node = value
        
class SinglyLinkedList
    """Defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        newNode = Node(value)
        #check if new node is less than head
        if self.__head is None:
            self.__head = newNode
        #check if next_node is larger than new node
        if self.__head.data < value:
            newNode.next_node = self.__head
            self.__head = newNode

            
        #check if we're at end of node
        #create new node with value
        #change existing next node to point to new node and new node to
        #point to next node if existing


