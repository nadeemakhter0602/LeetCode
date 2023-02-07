# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        while(n>=0):
            if fast!=None:
                fast = fast.next
            else:
                return head.next
            n-=1
        while(fast!=None):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head