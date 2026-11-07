# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        start, end = dummy, dummy
        for _ in range(n):
            end = end.next
        while end.next:
            start = start.next
            end = end.next
        start.next = start.next.next
        return dummy.next