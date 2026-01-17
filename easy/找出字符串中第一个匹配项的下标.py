class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i,ch in enumerate(haystack):
            if ch == needle[0]:
                if haystack[i:i+n] ==needle:
                    return i
        return -1            