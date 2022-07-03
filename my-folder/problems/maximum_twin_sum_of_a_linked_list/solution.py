# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans=list()
        l=head
        lenA=0
        while l:
            ans.append(l.val)
            l=l.next
            lenA=lenA+1
        maxsum=0
        l=head
        count=len(ans)-1
        while count >= len(ans)//2:
            if maxsum < (int(ans[count])+int(l.val)):
                maxsum = (int(ans[count])+int(l.val))
            l=l.next
            count=count-1
        return maxsum
            