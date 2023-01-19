class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp=[0]*(n+1)
        for i in range(0, len(dp)):
            if i%2==0:
                dp[i]=dp[i//2]
            else:
                dp[i]=1+dp[i//2]
        return dp