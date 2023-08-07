class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i]>=step:
                step = i
        if step ==0:
            return True 
        else:
            return False