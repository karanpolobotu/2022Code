# Linked List implementation of a stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    counter = 0

    def __init__(self):
        self.head = None

    def size(self):
        #working
        temp = self.head
        while (temp):
            self.counter += 1
            temp = temp.next

        return self.counter

    def top(self):
        #working
        temp = self.head
        return temp.data


    def pop(self):
        # return data item from top of stack and remove it from stack
        # storing the head node

        temp = self.head

        # edge case when deleting one and only node

        if (temp != None):
            self.head = temp.next
            temp = None
            print("Popped!")
            return 0

            # delete this instance
            prev = temp
            temp = temp.next

        if temp == None:
            return "Nothing to pop"

        prev.next = temp.next

        temp = None
        print("Popped!")
        return 0

    def push(self, item):
        # Add data item to last part of stack (LIFO)
        new_Node = Node(item)

        if self.head == None:
            self.head = new_Node
            return 0

        else:
            new_Node.next = self.head
            self.head = new_Node #(swap em out)

        return 0


    def is_empty(self):
        #working
        if self.head == None:
            return True

        return False

    def show(self):
        #working
        temp = self.head
        while (temp):
            print(temp.data, end = " ")
            temp = temp.next

if __name__ == "__main__":

    stacktest = Stack()
    print(stacktest.is_empty())
    print(stacktest.push(5))
    print(stacktest.show())
    stacktest.pop()
    print(stacktest.show())
    print("is empty: ", stacktest.is_empty())
    print(stacktest.show())
    stacktest.push(1)
    print(stacktest.show())
    stacktest.push(2)
    print(stacktest.show())
    stacktest.push(3)
    print(stacktest.show())
    stacktest.pop()
    print("Stack: ", stacktest.show())
    print("length: ", stacktest.size())
    print("is empty: ", stacktest.is_empty())
    print("top: ", stacktest.top())
    print("Stack: ", stacktest.show())
