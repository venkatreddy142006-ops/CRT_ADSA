# 1572. Matrix Diagonal Sum
'''
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i]
            total += mat[i][n - 1 - i]
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]
        return total
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum_optimal(mat))
'''