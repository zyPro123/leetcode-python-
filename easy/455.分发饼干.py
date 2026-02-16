from typing import List
"""假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；
并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，
我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
你的目标是满足尽可能多的孩子，并输出这个最大数值。"""
#这道题主要是贪心算法的入门，
#“用我当前最小的饼干，去满足我当前最容易满足的孩子。”
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #先使用内置的算法排好序列（当然，也可以自己写）
        g.sort()
        s.sort()

        child_ptr = 0
        cookie_ptr = 0
       #两个数列，两个“指针”
        while child_ptr<len(g) and cookie_ptr<len(s):
            if s[cookie_ptr]>=g[child_ptr]:
                child_ptr+=1

            cookie_ptr+=1
        return child_ptr