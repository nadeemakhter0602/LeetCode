# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        def merge(l1, l2):
            head = ListNode()
            dummy = head
            while l1!=None and l2!=None:
                if l1.val<l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            if l1!=None:
                dummy.next = l1
            elif l2!=None:
                dummy.next = l2
            return head.next
        def mergek(lists):
            while len(lists)>1:
                tmp = []
                for i in range(0, len(lists), 2):
                    l1 = lists[i]
                    l2 = lists[i+1] if i+1<len(lists) else None
                    tmp.append(merge(l1, l2))
                lists = tmp
            return lists[0]
        head = mergek(lists)
        return head