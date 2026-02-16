from typing import List
"""给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。
你在任何时候 最多 只能持有 一股 股票。然而，
你可以在 同一天 多次买卖该股票，但要确保你持有的股票不超过一股。

返回 你能获得的 最大 利润 。"""

class Solution:
    #方法一，状态机dp
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp_i_0 = 0
        dp_i_1 = -prices[0]

        for i in range(1,n):
            dp_i_0 = max(dp_i_0,dp_i_1+prices[i])
            #和121不一样的地方就在这里，它可以是之前的减去prices[i]
            dp_i_1 = max(dp_i_0-prices[i],dp_i_1)
        return dp_i_0
   #方法二，贪心算法优化
    def maxProfit_greedy(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit