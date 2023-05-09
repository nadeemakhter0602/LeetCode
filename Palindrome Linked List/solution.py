# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        reverse = None
        while fast != None:
            if not fast.next:
                slow = slow.next
                break
            fast = fast.next.next
            backup = slow.next
            slow.next = reverse
            reverse = slow
            slow = backup
        while slow != None:
            if reverse.val != slow.val:
                return False
            slow = slow.next
            reverse = reverse.next
        return True
