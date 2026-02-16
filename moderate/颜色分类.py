"""给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，
原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库内置的 sort 函数的情况下解决这个问题。"""
"仅使用常数空间的一趟扫描算法"

from typing import List
#这道题使用双指针的pro版本，三指针，本质是分类，左指针是0，右指针是2，即不是左也不是右就是1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right,curr = 0,len(nums)-1,0
        while curr<=right:
            if nums[curr]==2:
                nums[curr],nums[right] = nums[right],nums[curr]
                right-=1#这里不能先加，万一不是0呢
            elif nums[curr]==0:
                nums[curr],nums[left] = nums[left],nums[curr]
                left+=1
                curr+=1#当是0的时候可以同时一起加一
            else:
                curr+=1#这里就是1的情况