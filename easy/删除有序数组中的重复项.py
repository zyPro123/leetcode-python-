#这里使用双指针，当然不是止两个for循环
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        #处理边界情况，如果是空数组直接返回0
        if not nums:
            return 0
        slow = 0#慢指针，已排序好的末端
        for fast in range(1, len(nums)):#快指针，负责找不同的
            if nums[slow] != nums[fast]:
                nums[slow + 1] = nums[fast]
                slow += 1
                print(slow)

        slow += 1#由于最初的是0，所以这里加一个一

        return slow