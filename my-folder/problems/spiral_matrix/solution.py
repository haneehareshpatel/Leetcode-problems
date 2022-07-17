class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        top = 0
        bottom=len(matrix)
        right=len(matrix[0])
        left=0
        ans=list()
        while left < right and top<bottom:
            for x in range(left,right):
                ans.append(matrix[top][x])
            
            top+=1
            
            for y in range(top,bottom):
                ans.append(matrix[y][right-1])
            right-=1
            
            if not (left<right and top<bottom):
                break
            
            for q in range(right-1,left-1,-1):
                ans.append(matrix[bottom-1][q])
            bottom-=1
            
            for z in range(bottom-1,top-1,-1):
                ans.append(matrix[z][left])
            left+=1
            
        return ans
            
            
            