from typing import List
'''给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。'''
#这个是目前（2.8）做过最难的题目了，和正方形完全不是一个东西
#dp的使用更加的泛，而且是多个dp一起使用，甚至默认优化了
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m,n = len(matrix),len(matrix[0])

        height = [0]*n
        left = [0]*n
        right = [n-1]*n
        max_area = 0

        for i in range(m):
            #高度指的是第j列，以i为底的柱子高度
            for j in range(n):
                #注意，第二个height[j]其实是上一个，下面的两个dp也是干这个事情，
                height[j] = (height[j]+1) if matrix[i][j]=='1' else 0

            cur_left = 0
            #这里左边界和下面分开了，这样也好，但是意思其实一样的
            for j in range(n):
                if matrix[i][j]=='1':
                    left[j] = max(left[j],cur_left)
                else:
                    # 这里其实已经没有任何意义了，如果matrix[i][j]=='1'，也就是这里的height为0，取0只是为了不干扰下一次的计算
                    left[j] = 0
                    #下一个的左边界的索引至少是j+1
                    cur_left = j+1
            cur_right = n-1
            #右的话就要反过来
            for j in range(n-1,-1,-1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j],cur_right)
                else:
                    #和上面同理
                    right[j] = n-1
                    cur_right = j-1
            for j in range(n):
                #最后就是索引差×柱体高度
                width = right[j]-left[j]+1
                area = height[j]*width
                max_area = max(area,max_area)
        return max_area