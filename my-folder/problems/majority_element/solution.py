class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = Counter(nums)
        for x, y in dictionary.items():
            if y>math.floor(len(nums)/2):
                return x