206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/description/

Given the head of a singly linked list, reverse the list, and return the reversed list.

1. 迭代法 (常用且高效)迭代法的核心思路是：在遍历链表的过程中，将当前节点 curr 的 next 
指针指向它的前驱节点 prev。由于指向 prev 后会失去对原后继节点的引用，所以需要一个临时变量 
next_node 来提前保存。Python 代码实现Pythondef reverseList(head):
    prev = None
    curr = head
    
    while curr:
        # 1. 暂时保存当前节点的下一个节点
        next_node = curr.next
        # 2. 将当前节点指向它的前驱节点
        curr.next = prev
        # 3. prev 向前移动一步
        prev = curr
        # 4. curr 向前移动一步
        curr = next_node
        
    # 最后 prev 会指向原链表的最后一个节点，即新链表的头
    return prev
2. 递归法 (思路巧妙)递归法的精髓在于：假设 head 之后的链表已经全部反转好了，我们只需要把 head.next 
的 next 指向 head 自己，并将 head.next 置为空。Python 代码实现Pythondef reverseList(head):
    # 基准情况：如果链表为空或只有一个节点，直接返回
    if not head or not head.next:
        return head
    
    # 递归反转后面的链表
    new_head = reverseList(head.next)
    
    # 将 head.next (即反转后链表的尾部) 的 next 指向 head
    head.next.next = head
    # 防止链表成环，将 head.next 断开
    head.next = None
    
    return new_head
3. 复杂度与对比方法时间复杂度空间复杂度备注迭代法$O(n)$$O(1)$生产环境下最推荐，不消耗额外栈空间。
递归法$O(n)$$O(n)$空间复杂度主要来自递归调用的系统栈。