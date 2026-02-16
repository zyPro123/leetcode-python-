"""给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
注意：a + b 意味着字符串 a 和 b 连接。"""

#二维dp，使用的是自底向上的方法，可以优化成一维
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n = len(s1),len(s2)
        if m+n != len(s3):
            return False
        #这里是加1是因为可以空字符串和有字符串来比较，不是虚拟字符串
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        #这里是要边界判断，因为值不一样
        for i in range(1,m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]

        for j in range(1,n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1]==s3[j-1]

        for i in range(1,m+1):
            for j in range(1,n+1):
                k = i+j-1
                #dp[i][j] 表示：s1 的前 i 个字符和 s2 的前 j 个字符
                task_1 = dp[i][j-1] and s2[j-1]==s3[k]
                task_2 = dp[i-1][j] and s1[i-1]==s3[k]
                dp[i][j] = task_1 or task_2
        return dp[m][n]