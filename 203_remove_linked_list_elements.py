# 203. Remove Linked List Elements
# Difficulty - Easy
# https://leetcode.com/problems/remove-linked-list-elements/

# Remove all elements from a linked list of integers that have value val.

# Example: Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def removeElements(head, val):
    while head and head.val == val:
        head = head.next
    if not head:
        return head
    current = head
    while current.next:
        if current.next and current.next.val == val:
            current.next = current.next.next            
        else:
            current = current.next
    return  head

# Success - Details 
# Runtime: 64 ms, faster than 92.16% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 16.7 MB, less than 90.67% of Python3 online submissions for Remove Linked List Elements.

# Runtime: 72 ms, faster than 59.14% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 16.7 MB, less than 93.81% of Python3 online submissions for Remove Linked List Elements.