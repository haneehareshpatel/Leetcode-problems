class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_ans=0
        for i in range(1,len(strs)):
            count=0
            for j in range(0,len(strs[0])):
                if j < len(strs[i]):
                    if strs[i][j]==strs[0][j]:
                        count=count+1
                    else:
                        break
            if i==1:
                max_ans=count
            if count < max_ans:
                max_ans=count
        if len(strs) > 1:
            return strs[0][0:max_ans]
        else:
            return strs[0]