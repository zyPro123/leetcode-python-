from typing import List
'''给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。'''
class Solution:
    #dp,但是双向的，把left_max,right_max都搞出来
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0]*n
        right_max = [0]*n
        left_max[0] ,right_max[n-1]= height[0],height[n-1]
        for i in range(1,n):
            left_max[i] = max(height[i],left_max[i-1])
        for j in range(n-2,-1,-1):
            right_max[j] = max(height[j],right_max[j+1])
        sum = 0
        for i in range(n):
            #把每一个都抽象成水桶
            sum += min(left_max[i],right_max[i])-height[i]
        return sum
    #最初是双向dp，下面是用双指针优化了
'''def trap_double(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        sum = 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                sum += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                sum += right_max - height[right]
                right -= 1
        return sum'''