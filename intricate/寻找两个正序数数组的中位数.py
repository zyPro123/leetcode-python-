from typing import List
"""给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) """
#第一次作死做难题
"""递归终止条件（base case）：什么时候停止递归

递归调用（recursive call）：函数调用自己

向终止条件逼近：每次调用问题规模变小"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)

        if total % 2 == 1:  # 奇数
            return self.findKth(nums1, nums2, total // 2 + 1)
        else:  # 偶数
            left = self.findKth(nums1, nums2, total // 2)
            right = self.findKth(nums1, nums2, total // 2 + 1)
            return (left + right) / 2.0

    def findKth(self, nums1: List[int], nums2: List[int], k: int) -> float:
        """
        在两个有序数组中寻找第k小的数（k从1开始计数）
        """
        # 确保nums1是较短的数组，这样效率更高
        if len(nums1) > len(nums2):
            return self.findKth(nums2, nums1, k)#这里使用的递归（recursion）

        # 如果一个数组为空，直接从另一个数组返回第k个元素
        if not nums1:
            return nums2[k - 1]

        # 如果k=1，返回两个数组第一个元素的最小值
        if k == 1:
            return min(nums1[0], nums2[0])

        # 取两个数组的第k/2个元素（注意不要越界）
        i = min(len(nums1), k // 2)
        j = min(len(nums2), k // 2)

        # 比较并排除较小的那一部分
        if nums1[i - 1] < nums2[j - 1]:
            # 排除nums1的前i个元素
            return self.findKth(nums1[i:], nums2, k - i)
        else:
            # 排除nums2的前j个元素
            return self.findKth(nums1, nums2[j:], k - j)
