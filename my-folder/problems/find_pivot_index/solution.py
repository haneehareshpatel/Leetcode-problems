class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left=0
        sum_right=0
        
        for x in range(0,len(nums)):
            sum_right=sum_right+nums[x]
        
        for x in range(0,len(nums)):
            if x!=0:
                right=sum_right-sum_left-nums[x]
            else:
                right=sum_right-nums[0]
            if right==sum_left:
                return x
            sum_left=sum_left+nums[x]
        return -1
        