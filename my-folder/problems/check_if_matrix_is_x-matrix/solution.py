class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        flag=False
        for x in range(0,len(grid)):
            for y in range(0,len(grid[0])):
                if x!=y and y!=len(grid)-x-1 and grid[x][y]!=0:
                    return False
                if x==y and grid[x][y]==0:
                    return False
                if y==len(grid)-x-1 and grid[x][y]==0:
                    return False
        return True