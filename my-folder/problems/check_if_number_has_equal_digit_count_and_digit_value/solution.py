class Solution:
    def digitCount(self, num: str) -> bool:
        flag=True
        ans=dict()
        
        for x in range(0,len(num)):
            if num[x] not in ans.keys():
                ans[num[x]]=0
            ans[num[x]]=ans[num[x]]+1
        
        for x in range(0,len(num)):
            
            if str(x) not in ans.keys():
                if int(num[x])!=0:
                    flag=False
                    break
            elif int(ans[str(x)])!=int(num[x]):
                flag=False
                break
            else:
                pass
        return flag