from typing import List
"""有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。戳破第 i 个气球，
你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 
这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。
如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

求所能获得硬币的最大数量。"""

'''这道题如果顺着想，会有很多不可确定的问题，但是逆着来，最后一个气球肯定是要被戳破的
这时候我们就是要找到那个k，就能分解成两个小区间的最大数量，然后同理可得'''
#区间dp：是二维DP的一种，它特指那种状态定义在区间上，且通过合并小区间来求解大区间的二维DP问题
'''区间的体现就在这里，我们是要以范围来遍历，而不是顺着数组遍历'''

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 定义 dp[i][j] 为：戳破开区间 (i, j) 内部（即不包括i和j）的所有气球，能获得的最大分数。
        balloons = [1]+nums+[1]
        new_n = len(balloons)

        dp = [[0]*new_n for _ in range(new_n)]
        #这里是区间dp固定的格式
        for length in range(3,new_n+1):
            for i in range(0,new_n-length+1):
                j = i+length-1#我知道i，自然知道j
                for k in range(i+1,j):
                    coints = dp[i][k]+dp[k][j]+balloons[i]*balloons[k]*balloons[j]
                    dp[i][j] = max(dp[i][j],coints)
        return dp[0][new_n-1]