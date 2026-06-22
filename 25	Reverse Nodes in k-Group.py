
215. Kth Largest Element in an Array
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        prev_group_end = dummy
        
        while True:
            # 1. 找到当前组的结尾
            group_end = prev_group_end
            for _ in range(k):
                group_end = group_end.next
                if not group_end:
                    return dummy.next # 剩余不足 k 个，直接结束
            
            # 2. 记录下一组的开始，并断开当前组
            next_group_start = group_end.next
            group_start = prev_group_end.next
            group_end.next = None # 这一步能有效防止反转时产生环
            
            # 3. 反转当前组，并接回原链表
            # 反转后，原来的 start 变成 end，原来的 end 变成 start
            prev_group_end.next = self.reverse(group_start)
            
            # 4. 重新连接下一组，并移动 prev_group_end
            group_start.next = next_group_start
            prev_group_end = group_start
            
    # 辅助函数：标准反转链表（LC 206）
    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev