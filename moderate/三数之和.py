#转换成两数之和，只不过结果会变化而已，使用双指针来遍历（当然不是C语言那个指针）
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()#排序，关键

        result = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            target = -nums[i]
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum > target:
                    right -= 1
                else:
                    left += 1
        return result