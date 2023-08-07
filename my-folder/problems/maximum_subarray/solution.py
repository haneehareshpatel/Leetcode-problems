class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            ans = max(ans, curr_sum)
        return ans