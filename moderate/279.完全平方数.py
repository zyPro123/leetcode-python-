"""给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，
其值等于一个整数自乘的积。
例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。"""
#优化一维dp,完全背包问题
class Solution:
    def numSquares(self, n: int) -> float:
        # 赋值成无穷大，因为后面要比较并且这样减少内存占用
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        # 高效的写法
        squares = [i*i for i in range(1,int(n**0.5)+1)]

        for square in squares:
            for i in range(square,n+1):
                # dp[i]表示的是当数字为i的时候的最少数量
                dp[i] = min(dp[i],dp[i-square]+1)
        return dp[n]