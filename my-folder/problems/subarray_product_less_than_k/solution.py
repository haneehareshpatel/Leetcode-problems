class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        right =0
        product =1
        for i in range(0, len(nums)):
            product = product*nums[i]
            while product >=k and left <=i:
                product = product/nums[left]
                left = left +1
            count = count + (i-left+1)
        return count