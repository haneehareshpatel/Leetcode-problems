class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=-1
        last=-1
        for x in range(0,len(nums)):
            if nums[x]==target:
                first=x
                break
        
        count=len(nums)-1
        while count>=0:
            if nums[count]==target:
                last=count
                break
            count=count-1
        
        return [first,last]
        