#这也是一道双指针的题目，使用滑动窗口
"为了降低时间复杂度，用字典（或者列表）来记录之前的数据"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        max_len = 0
        char_dict = {}

        for right in range(len(s)):
            current_char = s[right]
            #字典和列表的好处，用in就可以了
            if current_char in char_dict and char_dict[current_char]>=left:
            #检查键和值
                left = char_dict[current_char]+1
            char_dict[current_char] = right#如何给字典赋值
            current_len = right-left+1

            if current_len>max_len:
                max_len = current_len
        return max_len