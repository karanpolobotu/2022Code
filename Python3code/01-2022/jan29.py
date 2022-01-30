
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # insert node before, at a given point or after all nodes in a Linked List

    def insertFront(self, item):
        new_Node = Node(item) # define new node
        new_Node.next = self.head # make new node as head
        self.head = new_Node # move the head to point to the new Node (swap)

    def insertAfter(self, prev_node, item):
        if prev_node == None:
            return "cannot insert in rear, rear does not exist"
        else:
            new_Node = Node(item) # define node
            new_Node.next = prev_node.next # new node is pointed to by previous node
            prev_node.next = new_Node # swap

    def insertRear(self, item):
        new_Node = Node(item) #define node

        if self.head == None: #edge case/empty List
            self.head = new_Node

        # traverse list till end and insert

        temp = self.head
        while(temp.next):
            temp = temp.next #cannot use direct self.head reference, creates issues

        # insert
        temp.next = new_Node

    def deleteNode(self, key):
        # storing the head node

        temp = self.head

        # edge case when deleting one and only node

        if (temp != None):
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # keep going through list until you get to the data to be deleted
        while (temp != None):
            if temp.data == key:
                break

            # delete this instance
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next

        temp = None

    def show(self):
        temp = self.head
        while (temp):
            print(temp.data, end = " ")
            temp = temp.next

if __name__ == "__main__":

    lList = LinkedList()
    lList.head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    lList.head.next = node2
    node2.next = node3

    print("before")
    lList.show()
    print()
    print("after")
    #lList.insertFront(0)
    #lList.insertAfter(node3, 0) #insert at given position
    lList.insertRear(4)
    lList.show()
