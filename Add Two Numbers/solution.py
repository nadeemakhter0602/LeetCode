# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = ListNode()
        s1 = s
        carry = 0
        while l1!=None and l2!=None:
            total = l1.val + l2.val + carry
            s1.next = ListNode(total % 10)            
            carry = 1 if total > 9 else 0
            l1 = l1.next
            l2 = l2.next                
            if l1 == None and l2 != None:
                l1 = ListNode()
            if l2 == None and l1 != None:
                l2 = ListNode()   
            s1 = s1.next                
        if carry > 0:
            s1.next = ListNode(carry)
        return s.next