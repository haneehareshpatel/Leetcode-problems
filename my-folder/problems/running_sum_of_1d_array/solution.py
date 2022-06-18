class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=list()
        sum=0
        for x in range(0,len(nums)):
            sum=sum+nums[x]
            ans.append(sum)
            
        return ans
            