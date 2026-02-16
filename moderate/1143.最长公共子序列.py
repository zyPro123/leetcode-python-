"""给定两个字符串 text1 和 text2，
返回这两个字符串的最长 公共子序列 的长度。
如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它
是由原字符串在不改变字符的相对顺序的情况下删除某些字符
（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。"""
#这个是动态规划的进阶，二维Dp
#使用二维是因为我需要通过它来同时反应两个数组
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)

        dp = [[0]*(n+1)for _ in range(m+1)]#m rows,n colums

        for i in range(1,m+1):
            for j in range(1,n+1):
                #状态转移方程

                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1#如果匹配，就是在之前的LCU加一
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])#无论如何，其中一个一定有
        return dp[m][n]