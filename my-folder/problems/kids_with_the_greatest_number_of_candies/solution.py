class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = 0
        for i in range(0, len(candies)):
            max_candy = max(max_candy, candies[i])
        ans = list()
        for i in range(0, len(candies)):
            if candies[i]+extraCandies >= max_candy:
                ans.append(True)
            else:
                ans.append(False)
        return ans