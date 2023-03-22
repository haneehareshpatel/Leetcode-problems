class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        curr_sum = 0
        ans =0
        for x in range(0, len(nums)):
            if nums[x]==0:
                curr_sum = curr_sum + 1
                ans = ans+ curr_sum
            else:
                curr_sum =0
        return ans