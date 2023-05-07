# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        first_half = []
        odd = False
        while fast != None:
            if fast.next != None:
                fast = fast.next.next
            else:
                fast = None
                odd = True
            first_half.append(slow.val)
            slow = slow.next
        if odd:
            first_half.pop()
        while slow != None:
            if first_half and first_half.pop() != slow.val:
                return False
            slow = slow.next
        return True
