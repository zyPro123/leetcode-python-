from typing import List
"""给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。"""

#状态机dp，一个值共有2*2个状态，最后总结的就是这四个状态下哪个最好
#为什么最初没有想出来，被最多两笔交易卡住了，不知道怎么转化
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0

        for p in prices[1:]:
            #这里优化了
            sell2 = max(sell2,buy2+p)
            buy2 = max(buy2,sell1-p)
            sell1 = max(sell1,buy1+p)
            buy1 = max(buy1,-p)
        return max(sell1,sell2)