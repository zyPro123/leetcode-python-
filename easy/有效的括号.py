#使用列表来模拟栈的操作，括号体现的就是栈先进后出的特点
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}#字典键和值来匹配

        stack = []
        for i in s:
            if i in pairs.values():#值刚好是左括号
                stack.append(i)
            elif i in pairs:#键刚好是右括号
                if not stack or stack.pop() != pairs[i]:
                    #pop返回最后的值，不带参数，但是不能对空的操作
                    return False

        return not stack#检测，确认栈里空了
s = ""
solution = Solution()
print(solution.isValid(s))