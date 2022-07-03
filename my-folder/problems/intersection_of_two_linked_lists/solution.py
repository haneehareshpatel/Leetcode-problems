# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA=0
        lenB=0
        la=headA
        lb=headB
        while la:
            lenA=lenA+1
            la=la.next
        while lb:
            lenB=lenB+1
            lb=lb.next
        diff=lenA-lenB
        la=headA
        lb=headB
        if diff<0:
            count=0
            while count<abs(diff):
                count=count+1
                lb=lb.next
        else:
            count=0
            while count < diff:
                count+=1
                la=la.next
        while la and lb:
            if la==lb:
                return la
            la=la.next
            lb=lb.next
        return None