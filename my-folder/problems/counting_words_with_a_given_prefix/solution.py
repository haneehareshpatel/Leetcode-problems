class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count=0
        for wr in words:
            ind=0
            flag=False
            for x in range(0,len(pref)):
                if wr[ind]==pref[x]:
                    flag=True
                    if ind+1 <len(wr):
                        ind+=1
                    else:
                        if x !=len(pref)-1:
                            flag=False
                        break
                else:
                    flag=False
                    break
            if flag:
                count+=1
        return count