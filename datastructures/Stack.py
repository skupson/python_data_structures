from Node import Node

class Stack:
    def __init__(self):
        self.length = 0
        self.top = None
        self.bottom = None

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def peek(self):
        return self.top.data

    def pop(self):
        if self.top is None:
            return None
        self.top = self.top.next
        self.length -= 1

    def items(self):
        counter = 0
        print(self.top.data)
        current_node = self.top.next
        while counter < self.length-1:
            print("|")
            print(current_node.data)
            counter += 1
            current_node = current_node.next

# Test cases
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.items()
my_stack.pop()
my_stack.items()


