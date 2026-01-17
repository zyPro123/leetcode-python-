#二分法，因为要求复杂度为O(log n),下标默认2，也就是说每运行一次搜索范围就减半
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        left,right = 0,n-1
        while left<=right:
            mid = (left+right)//2
            if target ==nums[mid]:
                return mid
            elif target<nums[mid]:
                right = mid-1
            elif target>nums[mid]:
                left = mid +1
        return left
solution = Solution()
print(solution.searchInsert([1,3,5,6],5))