class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[0]=0
        if n>=1:
            dp[1]=1
        if n>=2:
            dp[2]=1
        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]