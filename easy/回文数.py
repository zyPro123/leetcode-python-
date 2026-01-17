#直接把数字转换来比较
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        n = len(str_x)
        reverse_x = ['']*n#设一个等长度的空字符
        for i ,num in enumerate(str_x):
            reverse_x[n-1-i] = num
        return str_x ==''.join(reverse_x)#不能直接比较，会有问题