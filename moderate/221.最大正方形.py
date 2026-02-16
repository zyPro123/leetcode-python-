from typing import List
"""在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。"""
#二维dp更加丰富的用法
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m,n = len(matrix),len(matrix[0])
        #在左和上加两个虚拟数列，用来处理边界条件
        dp = [[0]*(n+1) for _ in range(m+1)]
        max_side = 0

        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]=="1":#因为是从1开始的，得减去1才匹配
                    # 正方形的判断准则两个边长和对角线
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    # 这里dp意思是以右下角开始的正方形
                    max_side = max(dp[i][j],max_side)
        return max_side*max_side