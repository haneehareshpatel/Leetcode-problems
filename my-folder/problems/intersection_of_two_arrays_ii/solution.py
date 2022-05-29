class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans=list()
        count=0
        x=-1
        while x<len(nums1):
            x+=1
            while count<len(nums2):
                if x<len(nums1) and nums1[x]<nums2[count]:
                    x+=1
                elif x<len(nums1) and nums1[x]==nums2[count]:
                    ans.append(nums1[x])
                    count+=1
                    break
                else:
                    count+=1
            
        return ans