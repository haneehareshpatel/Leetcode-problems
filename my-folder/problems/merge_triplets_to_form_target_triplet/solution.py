class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = set()
        for i in range(0,len(triplets)):
            if (triplets[i][0]>target[0]) or (triplets[i][1] > target[1]) or (triplets[i][2]>target[2]):
                continue
            for j in range(0,3):
                if triplets[i][j]==target[j]:
                    ans.add(j)
        if len(ans)>2:
            return True
        else:
            return False