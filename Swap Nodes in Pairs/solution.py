# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        dummy = ListNode(0, head)
        prev = dummy
        while (first and first.next):
            # store next element
            second = first.next
            # store next to next element
            third = first.next.next
            # point second element to first
            second.next = first
            # point first element to third
            first.next = third
            # point second element to dummy
            prev.next = second
            # move prev to first
            prev = first
            # move first to third
            first = third
        return dummy.next
