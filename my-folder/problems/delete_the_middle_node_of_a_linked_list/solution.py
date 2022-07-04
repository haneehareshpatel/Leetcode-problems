# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lenA=0
        l=head
        if head is None or head.next is None:
            return None
        while l:
            lenA+=1
            l=l.next
        
        l=head
        count=1
        while l:
            if count==(lenA//2):
                l.next=l.next.next
                break
            count+=1
            l=l.next
        return head