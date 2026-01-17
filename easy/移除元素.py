#用双指针，左指针和右指针，复杂度为1
class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left