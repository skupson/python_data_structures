"""
Example of a linked list
my_link_list = {
    "head": {
        "value": 10,
        "next": {
            "value": 5,
            "next": {
                "value": 16,
                "next": None
            }
        }
    }
}
"""
from Node import Node


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.length = 1

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        self.length += 1

    def get(self, index):
        if index >= self.length:
            print("Error: index out of bound")
            return None
        elif index == 0:
            return self.head.data
        current_index = 1
        current_node = self.head.next
        while True:
            if current_index == index:
                return current_node.data
            current_index += 1
            current_node = current_node.next

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index >= self.length:
            print("Error: index out of bound")
            return None
        current_index = 1
        if index == 0:
            self.prepend(value)
            return None
        previous_node = self.head
        current_node = self.head.next
        while True:
            if current_index == index:
                previous_node.next = new_node
                new_node.next = current_node
                self.length += 1
                return None
            current_index += 1
            previous_node = previous_node.next
            current_node = current_node.next

    def remove(self, index):
        if index > self.length:
            print("Error: index out of bound")
            return None
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
            return None
        current_index = 1
        previous_node = self.head
        current_node = self.head.next
        while True:
            if index == current_index:
                previous_node.next = current_node.next
                self.length -= 1
                return None
            previous_node = previous_node.next
            current_node = current_node.next
            current_index += 1

    def print_list(self):
        current_index = 0
        current_node = self.head
        while True:
            if current_index >= self.length:
                print("None")
                break
            print(f"{current_node.data} --> ", end=" ")
            current_index += 1
            current_node = current_node.next


class DoublyLinkedList(LinkedList):
    def __init__(self, data):
        self.head = Node(data)
        self.length = 1

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        new_node.previous = current_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node
        self.length += 1


# Test cases
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.print_list()



