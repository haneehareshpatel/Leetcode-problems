class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = Counter(nums)
        for x,y in dictionary.items():
            if y==1:
                return x