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


