# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        count = 0
        ptr = head
        length_lst = 0
        while ptr:
            length_lst +=1
            ptr=ptr.next
        ptr=head
        if n == length_lst:
            return head.next
        while count < length_lst - n-1:
            ptr=ptr.next
            count=count+1
        ptr.next = ptr.next.next
        return head