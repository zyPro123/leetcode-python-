#哈希表，用减法来做，找我之前有出现过这个数吗
class Solution:
    def twoSum(self, nums, target):
        num_dict={}
        for i,num in enumerate(nums):
            complement=target-num

            if complement in num_dict:#字典的好处
                return [num_dict[complement],i]

            num_dict[num] = i