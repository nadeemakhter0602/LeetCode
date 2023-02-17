# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        window = set()
        while head != None:
            window.add(id(head))
            if id(head.next) in window:
                return True
            head = head.next
        return False