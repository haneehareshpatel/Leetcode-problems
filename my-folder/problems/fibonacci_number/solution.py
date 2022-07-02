class Solution:
    def fib(self, n: int) -> int:
        ans=[0,1]
        for x in range(2,n+1):
            t=ans[x-1]+ans[x-2]
            ans.append(t)
        return ans[n]