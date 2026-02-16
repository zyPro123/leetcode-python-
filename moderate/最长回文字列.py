"""给你一个字符串 s，找到 s 中最长的 回文 子串。"""
#这里用了双指针的方法，从中间向两边扩散开（背向指针）
#缺点就是时间复杂度为O(n^2),最好的办法是用Manacher算法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s

        start,end = 0,0
        for i in range(len(s)):
            #这里用两个是因为有的回文数是偶数，有的是单数
            len1 = self.expand(s,i,i)
            len2 = self.expand(s,i,i+1)

            max_len = max(len1,len2)
            #对比来更新
            if max_len>end-start +1:
                end = i+max_len//2
                start = i-(max_len-1)//2

        return s[start:end+1]

    #为了方便，这里直接写成一个函数
    def expand(self,s:str,start:int,end:int)-> int:

        while start >=0 and end<len(s) and s[start]==s[end]:
            start-=1
            end+=1
        return end-start-1#返回的不是普通的子列，二是回文子列，因此不但不加1，还要再减1