class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for x in range(0,len(nums)):
            if nums[x]==target:
                return x
            if nums[x]>target:
                return x
            
        return len(nums)