# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=1
        right=n
        mid=1+(n-1)//2
        while left <=right:
            mid=left+((right-left)//2)
            if isBadVersion(mid):
                if (mid-1)==0:
                    return mid
                if (mid-1)!=0 and not isBadVersion(mid-1):
                    return mid
                else:
                    right=mid-1
                    
            else:
                left=mid+1
        return -1