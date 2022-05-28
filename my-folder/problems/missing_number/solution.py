class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        flag = False
        for x in range(0,len(nums)):
            if nums[x]!=x:
                flag=True
                return x
                
        if not flag:
            if nums[-1]!=len(nums):
                return len(nums)
            else:
                return None
            