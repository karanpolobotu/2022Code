# Singly Linked List based Queue implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    #classic node definition

class Queue:
    def __init__(self):
        self.head = None
        #Define default Queue

    def enqueue(self, item):
        #FI for First In, place element at rear of queue (O(n))
        new_Node = Node(item)
        temp = self.head

        if self.head == None:
            self.head = new_Node
            return 0

        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next

            temp.next = new_Node
            return 0

    def dequeue(self):
        #FO, for first out. replace first element at front of queue (O(1))

        if self.head == None:
            return "nothing to dequeue"

        else:
            prev = self.head
            self.head = self.head.next
            prev.next = self.head

        return "dequeued"

    def show(self):
        temp = self.head

        while(temp):
            print(temp.data, end = " ")
            temp = temp.next

if __name__ == "__main__":
    testQueue = Queue()
    testQueue.enqueue(5)
    print(testQueue.show())
    testQueue.dequeue()
    print(testQueue.show())
    testQueue.enqueue(1)
    print(testQueue.show())
    testQueue.enqueue(2)
    print(testQueue.show())
    testQueue.enqueue(3)
    print(testQueue.show())
    testQueue.dequeue()
    print(testQueue.show())
    testQueue.dequeue()
    print(testQueue.show())
    testQueue.dequeue()
    print(testQueue.show())
