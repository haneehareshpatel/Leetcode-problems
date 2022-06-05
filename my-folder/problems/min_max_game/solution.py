class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums)!=1:
            ans=list()
            for i in range(0,int(len(nums)/2)):
                if i%2==0:
                    ans.append(min(nums[2*i],nums[2*i+1]))
                else:
                    ans.append(max(nums[2*i],nums[2*i+1]))
            nums=ans
        return nums[0]
            