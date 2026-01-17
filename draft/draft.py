class Solution:
    def factorial(self, k:int) -> int:
        factorial = 1
        for i in range(k-1):
            factorial = factorial*(k-i)
        return factorial

    def uniquePaths(self, m: int, n: int) -> int:
        integrate = 0
        if m<n:
            reverse = n
            n = m
            m = reverse
        else:
            n = n-1
            for i in range(n):
                integrate = integrate+factorial(m)/(factorial(n-i)*factorial(m-n+i))

        return integrate