class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x=len(nums)
        z=len(set(nums))
        flag=True
        if x==z:
            flag=False
                    
        return flag