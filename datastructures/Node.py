class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.left = None
        self.right = None
        self.previous = previous
