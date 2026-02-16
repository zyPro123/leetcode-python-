from typing import List
"""恶魔们抓住了公主并将她关在了地下城 dungeon 的 右下角 。
地下城是由 m x n 个房间组成的二维网格。
我们英勇的骑士最初被安置在 左上角 的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数
（若房间里的值为负整数，则表示骑士将损失健康点数）；
其他房间要么是空的（房间里的值为 0），
要么包含增加骑士健康点数的魔法球
（若房间里的值为正整数，则表示骑士将增加健康点数）。

为了尽快解救公主，骑士决定每次只 向右 或 向下 移动一步。
返回确保骑士能够拯救到公主所需的最低初始健康点数。

注意：任何房间都可能对骑士的健康点数造成威胁，
也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。"""
#二维dp，自底向上，虚拟优化
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> float:
        if not dungeon:
            return 1
        m,n = len(dungeon),len(dungeon[0])
        #增加虚拟行和列
        dp = [[float('inf')]*(n+1) for _ in range(m+1)]

        dp[m][n-1] = dp[m-1][n] = 1
        #逆着遍历，因为是量最少，而不是路径最少
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                #这里dp[i][j]指的是从i,j出发需要多少生命值
                '''使用反向dp，正向dp表示的是从起点 (0,0) 到 (i,j) 所需的最小初始血量'''
                require = min(dp[i][j+1],dp[i+1][j])-dungeon[i][j]
                dp[i][j] = max(1,require)

        return dp[0][0]