"""给定一个表示 大整数 的整数数组 digits，其中 digits[i]
是整数的第 i 位数字。这些数字按从左到右，从最高位到最低位排列。
这个大整数不包含任何前导 0。
将大整数加 1，并返回结果的数字数组"""
#主要是考察列表的使用，逆着遍历
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if not digits:
            return []

        digits[-1]=1+digits[-1]
        n = len(digits)
        for i in range(n-1,-1,-1):#(start,stop,step)(stop)(start,stop)
            if i!=0 and digits[i]>=10:
                digits[i] = 0
                digits[i-1] +=1
            elif i==0 and digits[i]==10:
                digits[i] = 0
                digits = [1]+digits  #如何在开头添加，末尾的用.append(your_number)
        return digits