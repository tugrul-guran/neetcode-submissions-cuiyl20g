# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = None
        curr = None

        p1 = list1
        p2 = list2

        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                to_add = ListNode(p1.val)
                p1 = p1.next
            else:
                to_add = ListNode(p2.val)
                p2 = p2.next
            
            if head is None:
                head = to_add
                curr = to_add
            else:
                curr.next = to_add
                curr = curr.next

        leftover = p1 if p1 is not None else p2

        while leftover is not None:
            to_add = ListNode(leftover.val)

            if head is None:
                head = to_add
                curr = to_add
            else:
                curr.next = to_add
                curr = curr.next

            leftover = leftover.next

        return head