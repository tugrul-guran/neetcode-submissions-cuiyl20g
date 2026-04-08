# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        tmp = None

        while curr is not None:
            nxt = curr.next
            curr.next = tmp
            tmp = curr
            curr = nxt

        return tmp