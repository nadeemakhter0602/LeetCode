# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointers = set()
        while headA:
            pointers.add(id(headA))
            headA = headA.next
        while headB:
            if id(headB) in pointers:
                return headB
            headB = headB.next
