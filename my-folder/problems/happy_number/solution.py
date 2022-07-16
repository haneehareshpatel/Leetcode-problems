class Solution:
    def isHappy(self, n: int) -> bool:
        ans=set()
        while n!=1:
            sumans=0
            for x in str(n):
                sumans = sumans+(int(x)*int(x))
            n=sumans
            if n in ans:
                return False
            ans.add(n)
        return True