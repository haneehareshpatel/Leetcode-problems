# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans=""
        l=head
        while l:
            ans=ans+str(l.val)
            l=l.next
        count=len(ans)-1
        while count >=len(ans)//2:
            if head.val!=int(ans[count]):
                print(head.val)
                print(ans[count])
                return False
            head=head.next
            count=count-1
        return True