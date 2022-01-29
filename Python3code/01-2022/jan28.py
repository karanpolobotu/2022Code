# January 28th code, going to be working on Data Structures practices & Implementations

# Q2, implementing stack

# part 1: Linked List & array-based list


# Linked List implementation (implement through class)

# Linked List looks like: [A, B] --> [B, C] --> [C, NULL]

# composed of 1) head and tail, the head is being pointed to, tail contains data (in DLL tail is prev elem)

# Advantage of LL, Dynamic size and Easy Insertion/deletion

# Disadvantages of LL, No random access allowed, extra memory space for pointer required w/ each element in list, not cache friendly

class Node:
    #each node contains data and a pointer to the next part of the list
    def __init__(self, data):
        self.data = data # data definition
        self.next = None # point to next datapoint

        # constructor in this case can be thought of as assigning default values for variables not included in object calls

class LinkedList:
    def __init__(self):
        self.head = None # defining what the head looks like. At each point, head is null

    def show(self):
        # function to print out linked list
        temp = self.head # current value
        while (temp): #while current value
            print(temp.data, end = " ") # print data
            temp = temp.next # go to next


if __name__ == "__main__":


    # classic array implementation
    print("array based implementation")
    array = [1, 2, 3, 4]
    print(array)
    array.append(5)
    print(array)
    array.remove(5)
    print(array)

    lList = LinkedList() # define linked list
    lList.head = Node(1) # LL sets default head to none, so if we are actually implemnting LL, must define head
    item2 = Node(2) # define second node
    item3 = Node(3) # define item three

    # Currently we have:  [1, NONE] --> [2, NONE] --> [3, NONE]

    # we want: [1, 2] --> [2, 3] --> [3, NONE]

    # Link the list together

    lList.head.next =  item2 # remember that next points to next data type, so we define it as such. Link item 1 and 2

    item2.next = item3 # Link Item 2 and 3

    print("Linked List traversal")
    lList.show()
