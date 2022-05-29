class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        l = list(s)
        d = dict()
        for x in s:
            if x not in d.keys():
                d[x]=0
            d[x]=d[x]+1
        minans=99999999
        flag=False
        target=list(target)
        t=Counter(target)
        for s in t.keys():
            if s in d.keys() and t[s]<=d[s]:
                flag=True
                if minans>(d[s]//t[s]):
                    minans=d[s]//t[s]
            
            else:
                minans=0
        return minans
        