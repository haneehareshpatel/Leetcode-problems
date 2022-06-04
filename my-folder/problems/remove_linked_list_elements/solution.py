# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head==None:
            return head
        if head.next==None and head.val==val:
            return None
        prev=None
        curr=head
        while curr:
            if curr.val==val and curr==head:
                head=head.next
            elif curr.val==val:
                 prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return head
        
        