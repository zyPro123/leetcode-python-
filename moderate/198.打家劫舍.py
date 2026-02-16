from typing import List

"""你是一个专业的小偷，计划偷窃沿街的房屋。
每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，
计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。"""

"""动态规划的三大支柱
最优子结构（Optimal Substructure）
大问题的最优解 = 小问题的最优解 + 某种组合
例如：爬楼梯中，f(n) = f(n-1) + f(n-2)

重叠子问题（Overlapping Subproblems）
在求解过程中，许多子问题会被重复计算多次
例如：计算f(5)时，f(3)会被多次用到

无后效性（Markov Property）
未来的状态只取决于当前状态，与过去的历史无关
例如：到达第n阶的方法数只取决于n-1和n-2阶，不关心你是怎么到n-1阶的"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        #边缘的情况列出来
        if n==0:
            return 0
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        #最初的形态
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])#状态转移方程

        return dp[n-1]