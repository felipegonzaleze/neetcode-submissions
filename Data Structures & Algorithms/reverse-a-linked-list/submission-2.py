# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head is not None:
            nxt = head.next # Next node
            head.next = prev # curr.next node is prev node
            prev = head # prev node is going to be curr node
            head = nxt
        return prev