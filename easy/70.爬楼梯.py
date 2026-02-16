"""假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？"""

#动态规划入门
#自底向上：从最小的子问题开始，逐步构建大问题的解。
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        #因为还有0，所以多了一个，感觉就是为了方便表示1就是第一阶
        dp =[0]*(n+1)
        dp[1] =1
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]#这里从底部开始记录，然后高的就是又底部来衍生的
        return dp[n]