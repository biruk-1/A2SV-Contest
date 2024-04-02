class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        myMatrix = [[0]*(n-2) for _ in range(n-2)]  

        for i in range(0, n-2):
            for j in range(0, n-2):
                maxNum = float('-inf')

                for x in range(3):
                    for y in range(3):
                        maxNum = max(maxNum, grid[i+x][j+y])

                myMatrix[i][j] = maxNum

        return myMatrix


