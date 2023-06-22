class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ans = dict()
        for i in range(0, len(nums)):
            if nums[i] in ans.keys() and abs(ans[nums[i]]-i)<=k:
                return True
            else:
                ans[nums[i]]=i
        return False