# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        curr=head
        if head is None or head.next is None:
            return None
        while curr:
            count=count+1
            curr=curr.next
        pos=count-n
        if pos==0:
            return head.next
        
        curr=head
        count=1
        while curr:
            if count==pos:
                curr.next=curr.next.next
            curr=curr.next
            count=count+1
        return head