# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        if head is None or head.next is None:
            return head
        curr=head
        rhead=head.next
        nt=curr.next
        while curr and curr.next:
            curr.next=curr.next.next
            nt.next=curr
            if prev_node:
                prev_node.next=nt
            prev_node=curr
            curr=curr.next
            nt=curr.next if curr is not None else None
        return rhead
            