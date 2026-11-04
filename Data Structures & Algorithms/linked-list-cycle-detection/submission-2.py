# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = []
        curr = head
        if not head:
            return False
        while True:
            if curr in nodes:
                return True
            else:
                nodes.append(curr)
            if curr.next:
                curr = curr.next
            else:
                return False
        return False