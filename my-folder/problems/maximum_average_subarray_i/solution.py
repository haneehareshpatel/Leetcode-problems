class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        count = 0
        left = 0
        sumans = 0
        maxavg = float("-inf")
        for i in range(0, len(nums)):
            sumans = sumans + nums[i]
            while (i-left+1)>k and left <i:
                sumans = sumans - nums[left]
                left = left + 1
            if (i-left+1)==k:
                maxavg = max(maxavg, (sumans/(i-left+1)))
        return maxavg