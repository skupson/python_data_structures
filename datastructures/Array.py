class Array:
    def __init__(self):
        self.data = {}
        self.length = 0

    def push(self, value):
        self.data[self.length] = value
        self.length += 1
        return self.length

    def get(self, index):
        current = 0
        while current <= self.length:
            if self.data.get(index) == self.data.get(current):
                print(self.data.get(index))
                break
            current += 1

    def values(self):
        if self.length == 0:
            print("[]")
            return None
        counter = 0
        print("[", end=" ")
        while counter <= self.length:
            print(f"{self.data.get(counter)}", end=",")
            counter += 1
        print("]", end="\n")

    def pop(self):
        del self.data[(self.length - 1)]


# Testing
my_array = Array()
my_array.values()
print(my_array.data)
