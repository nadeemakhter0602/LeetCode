# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        occured = set()
        h = head
        prev = None
        while head:
            if head.val in occured:
                prev.next = head.next
            else:
                occured.add(head.val)
                prev = head
            head = head.next
        return h
