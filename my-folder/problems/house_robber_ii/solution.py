class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        def helper(nums):
            dp = [0]*(len(nums)+1)
            if nums:
                dp[1]=nums[0]
            for x in range(1,len(nums)):
                dp[x+1]=max(dp[x],dp[x-1]+nums[x])
            return dp[-1]
        
        return max(helper(nums[0:-1]),helper(nums[1:]))