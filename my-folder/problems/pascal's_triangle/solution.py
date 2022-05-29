class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=list()
        ans.append([1])
        for x in range(1,numRows):
            temp=list()
            temp.append(ans[x-1][0])
            for z in range(1,x):
                if z<len(ans[x-1]):
                    temp.append(ans[x-1][z-1]+ans[x-1][z])
            temp.append(ans[x-1][-1])
            ans.append(temp)
        return ans