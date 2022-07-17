class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ans=""
        flag=False
        count=0
        if len(strs)==1:
            return strs[0]
        while count < len(strs[0]):
            for x in range(1,len(strs)):
                if count < len(strs[x]) and strs[0][count]==strs[x][count]:
                    flag=True
                else:
                    flag=False
                    break
            if not flag:
                break
            count+=1
        return strs[0][0:count]
    