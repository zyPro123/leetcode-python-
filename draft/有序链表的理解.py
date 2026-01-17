# 1. 先定义节点类（题目已给出）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
a = 5
b = None
b = a


# 手动创建一个简单的链表: 1 -> 2 -> 3
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

# 创建dummy节点，连接到这个链表
dummy = ListNode(0, node1)  # dummy.val=0, dummy.next=node1

print("=== 真实情况 ===")
print(f"1. dummy 本身: {dummy}")
print(f"   dummy 的类型: {type(dummy)}")
print(f"   dummy.val: {dummy.val}")
print(f"   dummy.next: {dummy.next} (这是node1的内存地址)")

print(f"\n2. dummy.next 是什么?")
print(f"   dummy.next == node1 ? {dummy.next is node1}")  # True
print(f"   dummy.next.val: {dummy.next.val}")  # 1

print(f"\n3. 通过dummy能访问到的所有节点:")
print(f"   dummy.next.val: {dummy.next.val}")          # 1
print(f"   dummy.next.next.val: {dummy.next.next.val}")    # 2
print(f"   dummy.next.next.next.val: {dummy.next.next.next.val}")  # 3

print(f"\n4. 现在模拟LeetCode的转换过程:")
def leetcode_style_convert(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 注意！LeetCode拿到的是你的 dummy.next，不是dummy本身！
linked_list_head = dummy.next  # 这就是你return的东西
converted_list = leetcode_style_convert(linked_list_head)
print(f"   LeetCode拿到的是: dummy.next = {linked_list_head}")
print(f"   LeetCode转换后输出: {converted_list}")
print(f"   但dummy本身仍然是: {dummy}")
print(f"   dummy.val仍然是: {dummy.val}")