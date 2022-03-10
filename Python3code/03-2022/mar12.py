# Leetcode, deleting duplication of list: https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        #edge cases
        if head == None or head.next == None:
            return head

        prev = head
        temp = head.next

        while temp != None:
            if prev.val == temp.val:
                prev.next = temp.next
                temp = prev.next
            else:
                temp = temp.next
                prev = prev.next

        return head

if __name__ == "__main__":
    test_list = ListNode(1)
    test_list.next = ListNode(1)
    test_list.next.next = ListNode(2)
    test_list.next.next.next = ListNode(3)
    test_list.next.next.next.next = ListNode(3)

    test_obj = Solution()
    print(test_obj.deleteDuplicates(test_list))
