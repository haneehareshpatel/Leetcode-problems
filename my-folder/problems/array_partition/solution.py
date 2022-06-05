class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sumans=0
        for x in range(0,len(nums)):
            if x%2==0:
                sumans=sumans+nums[x]
        return sumans