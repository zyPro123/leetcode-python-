"""给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。

左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。"""
#dp的应用
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N, dp = len(s), [0]*(len(s)+1)#虚拟长度，减少边界判断
        result = 0
        for i, c in enumerate(s):
            if c == '(' or i==0:
                continue
            if s[i-1]=='(':
                dp[i+1] = 2+dp[i-1]
            #三个条件判断，非0，不越界
            elif dp[i]>0 and i-1-dp[i]>=0 and s[i-1-dp[i]]=='(':
                # 前面会漏掉，所以要加上，这也是dp的好处之一，把大问题拆成小问题
                dp[i+1] = 2+dp[i]+dp[i-1-dp[i]]
            #最大值录入技巧
            result = max(result, dp[i+1])
        return result