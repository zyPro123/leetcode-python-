from typing import List

"""给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。"""
#状态机dp
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        n = len(prices)
        #最大也不会超过n//2，如果超了，就是随意买卖
        if k >= n // 2:
            # 直接使用第122题的贪心算法
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit
        dp0 = [0] * (k + 1)
        dp1 = [-prices[0]] * (k + 1)  # 初始化与三维版本逻辑一致

        for price in prices[1:]:  # 从第二天开始
            # 注意：内层循环需要从k倒序遍历，防止使用“今天”已更新的值
            for k_i in range(k, 0, -1):
                # 状态转移
                dp0[k_i] = max(dp0[k_i], dp1[k_i] + price)
                # 注意这里dp0[k_i-1]是昨天（更新前）的值，因为我们是倒序遍历
                dp1[k_i] = max(dp1[k_i], dp0[k_i - 1] - price)
        return dp0[k]