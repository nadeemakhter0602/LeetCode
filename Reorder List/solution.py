# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # function to reverse linked list
        def reverse(head):
            reverse = None
            while head != None:
                backup = head.next
                head.next = reverse
                reverse = head
                head = backup   
            return reverse
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next
            fast = fast.next
            slow = slow.next
        l2 = slow.next
        slow.next = None
        l2 = reverse(l2)
        l1 = head
        # zipper two halves
        while l1 != None and l2 != None:
            backup = l1.next
            l1.next = l2
            l1 = l1.next
            l2 = backup
        if l2 != None:
            l1.next = l2