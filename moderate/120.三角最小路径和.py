from typing import List
"""给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 
相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，
如果正位于当前行的下标 i ，
那么下一步可以移动到下一行的下标 i 或 i + 1 。

 """
#动态规划，本来是用二维，这里优化了，使用一维
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        n = len(triangle)
        dp = triangle[-1][:]#最正确的赋值方法

        for i in range(n - 2, -1, -1):#(start,stop,step),这里是逆遍历，能够少去很多边界情况
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]#个人理解是只有这里才会到triangle[0][0]，我们毕竟是逆着来的