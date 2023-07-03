class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[],[]]
        for i in range(0,len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in ans[0]:
                ans[0].append(nums1[i])
        for i in range(0, len(nums2)):
            if nums2[i] not in nums1 and nums2[i] not in ans[1]:
                ans[1].append(nums2[i])
        return ans