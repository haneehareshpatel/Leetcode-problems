class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count=0
        for x in range(0,len(nums1)):
            if count < n and nums1[x]>nums2[count]:
                nums1[x+1:]=nums1[x:]
                nums1[x]=nums2[count]
                count=count+1
        if count<n:
            nums1[(m+count):]=nums2[count:]
        x = len(nums1)-1
        while x>=0:
            if nums1[x]==0:
                nums1.pop()
            else:
                break
            x-=1
        while len(nums1)!=(m+n):
            nums1.append(0)
            
        return nums1