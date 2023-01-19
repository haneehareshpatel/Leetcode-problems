class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp=[1]*(rowIndex+1)
        fact=[1]*(rowIndex+1)
        for i in range(1,rowIndex+1):
            fact[i]=i*fact[i-1]
        print(fact)
        for i in range(0, rowIndex+1):
            dp[i]=fact[rowIndex]/((fact[rowIndex-i])*(fact[i]))
        return dp