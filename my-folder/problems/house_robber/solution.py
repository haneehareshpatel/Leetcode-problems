class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*(len(nums)+1)
        dp[1]=nums[0]
        for x in range(1,len(nums)):
            dp[x+1]=max(dp[x],dp[x-1]+nums[x])
        return dp[-1]