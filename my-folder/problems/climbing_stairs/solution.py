class Solution:
    def climbStairs(self, n: int) -> int:
        ans=[0,1,2]
        for x in range(3,n+1):
            t=ans[x-1]+ans[x-2]
            ans.append(t)
        return ans[n]