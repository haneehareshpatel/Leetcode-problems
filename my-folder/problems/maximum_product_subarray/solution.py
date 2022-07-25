class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max=nums[0]
        curr_min=nums[0]
        max_prod = nums[0]
        
        for x in range(1,len(nums)):
            temp=max(curr_min*nums[x],curr_max*nums[x],nums[x])
            curr_min = min(curr_min*nums[x],curr_max*nums[x],nums[x])
            curr_max = temp
            max_prod=max(curr_max,max_prod)
        return max_prod
        
        