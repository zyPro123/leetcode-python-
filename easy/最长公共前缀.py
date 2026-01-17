class Solution:
    def longestCommonPrefix(self, strs: str) :
        if not strs or not strs[0]:
            return ""

        n = len(strs)
        for j,s in enumerate(strs[0]) :
            print(j)
            for i in range(1,n):
                if j >= len(strs[i]) or strs[i][j] != s:
                    return strs[0][:j]

        return strs[0]
strs = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs))