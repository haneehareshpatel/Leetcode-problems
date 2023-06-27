# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 0
        curr_head = head
        while curr_head:
            length = length + 1
            curr_head = curr_head.next
        k = k%length
        if k==0:
            return head
        curr_head = head
        count = 1
        while curr_head and count<length -k:
            curr_head = curr_head.next
            count = count +1
        temp = curr_head.next
        curr_head.next = None
        curr = temp
        while temp and temp.next:
            temp=temp.next
        if temp :
            temp.next = head
        return curr
