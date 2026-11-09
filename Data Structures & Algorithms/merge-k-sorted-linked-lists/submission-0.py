# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq, itertools

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = itertools.count()
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, next(counter), node))
        dummy = ListNode()
        tail = dummy
        while heap:
            minNode = heap[0][2]
            tail.next = minNode
            tail = tail.next
            if minNode.next:
                heapq.heapreplace(heap, (minNode.next.val, next(counter), minNode.next))
            else:
                heapq.heappop(heap)
        return dummy.next