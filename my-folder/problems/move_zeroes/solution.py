class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzeroidx=0
        x=0
        while x < len(nums):
            if nums[x]!=0:
                nums[x],nums[nonzeroidx]=nums[nonzeroidx],nums[x]
                nonzeroidx+=1
            x+=1
            