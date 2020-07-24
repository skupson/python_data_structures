'''
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
'''


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


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
        current_index = 1
        if index == 0:
            self.prepend(value)
        previous_node = self.head
        current_node = self.head.next
        while True:
            if current_index == index:
                previous_node.next = new_node
                new_node.next = current_node
                return None
            current_index += 1
            previous_node = previous_node.next
            current_node = current_node.next



# Test cases
my_linked_list = LinkedList(12)
my_linked_list.append(4)
my_linked_list.append(6)
print(my_linked_list.get(2))
my_linked_list.prepend(7)
print(my_linked_list.get(0))
my_linked_list.insert(1, 13)
print(my_linked_list.get(1))

