class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for x in range(0,len(nums)):
            for y in range(0,len(nums)):
                if x!=y:
                    sum = nums[x]+nums[y]
                    if sum == target:
                        return [x,y]
                
