# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        
        mid=count//2
        
        count=0
        while head:
            if count==mid:
                return head
            count=count+1
            head=head.next