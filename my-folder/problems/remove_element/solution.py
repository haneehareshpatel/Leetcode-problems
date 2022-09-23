class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indx = 0
        for x in range(0, len(nums)):
            if nums[x]!=val:
                nums[indx]=nums[x]
                indx+=1
        return indx