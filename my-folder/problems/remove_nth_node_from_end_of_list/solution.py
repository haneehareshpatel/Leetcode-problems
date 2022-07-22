# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        later=head
        if head is None or head.next is None:
            return None
        if head.next.next is None:
            if n==1:
                head.next=None
                return head
            else:
                return head.next
        ctr=0
        while ctr<n:
            start=start.next
            ctr+=1
        if start is None:
            return head.next
        while start.next:
            later=later.next
            start=start.next
        later.next=later.next.next
        return head