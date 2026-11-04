# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        helper = []
        current_node = head
        if head is None:
            return head
        while True:
            helper.append(current_node.val)
            if current_node.next is None:
                break
            current_node = current_node.next
        current_node = head
        for i in range(len(helper) - 1, -1, -1):
            current_node.val = helper[i]
            current_node = current_node.next
        return head