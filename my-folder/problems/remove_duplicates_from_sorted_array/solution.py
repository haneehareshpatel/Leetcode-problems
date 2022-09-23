class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        indexunq = 1
        for i in range(0, len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[indexunq]=nums[i+1]
                indexunq =indexunq+1

        return indexunq