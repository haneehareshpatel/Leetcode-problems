import math
class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        curr = current.split(":")
        corr = correct.split(":")
        c = [1,5,15,60]
        if int(corr[0])-int(curr[0]) >= 0 and int(corr[1])-int(curr[1]) >= 0:
            time_diff = abs(int(corr[0])-int(curr[0]))*60+ abs(int(corr[1])-int(curr[1]))
        else:
            time_diff = abs(int(corr[0])-int(curr[0]))*60 - abs(int(corr[1])-int(curr[1]))
        dp = [time_diff+1]*(time_diff+1)
        dp[0]=0
        for x in range(1,len(dp)):
            for y in c:
                if x-y>=0:
                    dp[x]=min(dp[x],1+dp[x-y])
        if dp[-1]!=time_diff+1:
            return dp[-1]
        else:
            return -1