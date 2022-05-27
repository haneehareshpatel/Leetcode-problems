class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans1=list()
        ans2=list()
        for x in range(0,len(nums)):
            if nums[x]%2==0:
                ans1.append(nums[x])
            else:
                ans2.append(nums[x])
        for x in ans2:
            ans1.append(x)
        return ans1