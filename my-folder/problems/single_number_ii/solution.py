class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = Counter(nums)
        for i, j in ans.items():
            if j == 1:
                return i