class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea =0
        left , right = 0, len(height)-1
        while left < right:
            maxarea = max(maxarea, (right-                      left)*min(height[left],height[right]))
            if height[left]>height[right]:
                right = right -1
            else:
                left=left+1
        return maxarea