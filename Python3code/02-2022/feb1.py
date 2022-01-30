# Inbuild array based Queue implementation

class Queue:
    #FIFO data structure, #CHECK FOR EDGE CASES
    queue = []

    def enqueue(self, item):
        #add elements at beginning of list
        self.queue.append(item)
    def dequeue(self):
        temp = self.queue[0]
        #pop element at the start and remove it
        print("top element", temp)
        self.queue = self.queue[1:len(self.queue) - 1]
        return 0
    def show(self):
        print(self.queue)

if __name__ == "__main__":
    #enqueue, dequeue, show and front (peek to look at the first element)

    testQueue = Queue()
    testQueue.enqueue(5)
    testQueue.show()
    testQueue.dequeue()
    testQueue.show()
