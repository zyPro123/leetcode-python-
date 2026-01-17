#Optional[X] 等价于 Union[X, None]
#Definition for singly-linked list.
def convert_to_list(head_node):
    result = []
    current = head_node  # head_node就是你的dummy.next
    while current:
        result.append(current.val)  # 取出当前节点的值
        current = current.next  # 顺着next找到下一个节点
    return result  # 输出 [1, 2, 3]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        dummy = ListNode()
        current = dummy#要很好的理解‘=’，并非赋值，是将指针指向了一个值
        #其次，为什么叫链，是因为next，导致了它和下一个有着脱不了的干系，不是不变，
        # 而是变的很subtle，看不到的变
        while list1 is not None and list2 is not None:
            if list1.val >= list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next

        if list1 is not None:
            current.next = list1
        else:
            current.next = list2
        return dummy.next#这里需要处理才能看到
