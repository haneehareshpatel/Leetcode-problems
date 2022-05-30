class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)):
            min=nums[i]
            for j in range(i,len(nums)):
                if nums[j]<min:
                    x=nums[j]
                    min=nums[j]
                    nums[j]=nums[i]
                    nums[i]=x
        return nums
                    