class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for x in range(0,len(nums)):
            curr_sum = max(curr_sum+nums[x], nums[x])
            max_sum = max(curr_sum,max_sum)
        return max_sum