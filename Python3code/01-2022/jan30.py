#implementing built in array stack

class Stack:

    array = []

    def __init__(self):
        return None

    def is_empty(self):
        if len(self.array) == 0:
            return True
        return False

    def push(self, input):
        self.array.append(input)
        return 0

    def pop(self):
        if len(self.array) == 0:
            return "list empty"

        print("top of stack", self.array[0])
        self.array = self.array[1: len(self.array) - 1]
        return self.array

    def top(self):
        if len(self.array) == 0:
            return "list empty"
        return self.array[0]

    def size(self):
        return len(self.array)

    def show(self):
        return self.array

if __name__ == "__main__":

    stacktest = Stack()
    stacktest.push(5)
    print(stacktest.show())
    stacktest.pop(5)
    print(stacktest.show())
    print("is empty: ", stacktest.is_empty())
    stacktest.push(1)
    stacktest.push(2)
    stacktest.push(3)
    print("Stack: ", stacktest.show())
    print("length: ", stacktest.size())
    print("is empty: ", stacktest.is_empty())
    print("top: ", stacktest.top())
    print("Stack: ", stacktest.show())
