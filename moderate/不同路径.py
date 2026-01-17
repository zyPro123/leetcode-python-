#这就是道数学题而已，总共要走m+n-1步，挑出min(m-1,n-1)进行组合就行了
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        total_steps = m+n-2
        k = min(m-1,n-1)
        result = 1
        for i in range(1, k + 1):
            result = result * (total_steps - k + i) // i

        return result