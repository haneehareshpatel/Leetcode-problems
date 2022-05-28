class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter=0
        d=Counter(nums)
        for x in nums:
            d[x]=d[x]-1
            if d[x]>=0 and (k-x) in d.keys() and d[k-x]>0:
                counter+=1
                d[k-x]=d[k-x]-1
                
        return counter