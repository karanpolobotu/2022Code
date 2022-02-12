# I DID IT, LINKED LIST IMPLEMENTATION OF A MERGED LIST

# NOTE, THIS CODE PROBABLY WILL NOT RUN IN YOUR COMPILER, RUN IT ON THE LEETCODE COMPILER FOR THE PROBLEM SET

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Edge case, where either are empty lists

        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        # List initialization
        # Initialization is separate. If done in for loop, would continuously initialize the same thing
        if list1.val > list2.val:
            dNode = ListNode(list2.val)
            list2 = list2.next

        else:
            dNode = ListNode(list1.val)
            list1 = list1.next


        def addNode(cNode, a):
            #method to add the node at the end of the list
            aNode = ListNode(a)
            temp = cNode

            while(temp.next != None):
                temp = temp.next

            temp.next = aNode
            return 0


        temp1 = list1
        temp2 = list2

        while temp1 != None and temp2 != None:
            #compare values side by side, lower value goes in first
            if temp1.val > temp2.val:
                addNode(dNode, temp2.val)
                temp2 = temp2.next
            else:
                addNode(dNode, temp1.val)
                temp1 = temp1.next

        while temp1 != None:
            #to account for mistmatching lists (ex. list1 is of size 5, sorts but list 2 is of size 6. What happens to element 6 in list2?)
            addNode(dNode, temp1.val)
            temp1 = temp1.next

        while temp2 != None:
            addNode(dNode, temp2.val)
            temp2 = temp2.next

        return dNode
