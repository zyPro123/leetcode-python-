from typing import Optional
#使用链表，这道题模拟我们手算加法，逆序
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        #这里用carry的一个原因是99+1 = 100，但是这是三位数，carry是唯一一个不是0的
        while l1 or l2 or carry:
            #有长短之分，所以要判断一下
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10
            #这里就描述了怎样连接新节点，
            current.next = ListNode(digit)#val= digit，next= none
            current = current.next#val = dight,next = current

            if l1:#检查l1变量是否指向一个对象
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next