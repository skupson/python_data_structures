from Node import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.first is not None:
            return self.first.data
        else:
            return None

    def enqueue(self, value):
        new_node = Node(value)
        if self.last is not None:
            self.last.next = new_node
            self.last = new_node
        else:
            self.first = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.first is not None:
            self.first = self.first.next
        else:
            print("Error: the queue is empty")
            raise IndexError
        self.length -= 1

    def isempty(self):
        return not(bool(self.length))


# Test cases
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(4)
my_queue.enqueue(8)
print(f"First {my_queue.first.data}, Last: {my_queue.last.data}, Length: {my_queue.length}")
print(f"{my_queue.first.next}")
my_queue.dequeue()
print(f"First {my_queue.first.data}, Last: {my_queue.last.data}, Length: {my_queue.length}")
my_queue.dequeue()
print(f"First {my_queue.first.data}, Last: {my_queue.last.data}, Length: {my_queue.length}")
my_queue.enqueue(10)
print(f"First {my_queue.first.data}, Last: {my_queue.last.data}, Length: {my_queue.length}")