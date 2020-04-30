# 21. Merge Two Sorted Lists (Linked Lists)
# Difficulty - Easy
# https://leetcode.com/problems/merge-two-sorted-lists/

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example: Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode('Head')
    tail = l3
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            tail = tail.next
            l1 = l1.next
        else:
            tail.next = l2
            tail = tail.next
            l2 = l2.next
    
    if l1:
        tail.next = l1
    
    if l2:
        tail.next = l2

    return l3.next

# Success - Details
# Runtime: 28 ms, faster than 97.31% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.6 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.

# Runtime: 36 ms, faster than 68.02% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.9 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.

# Runtime: 40 ms, faster than 35.94% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.

# Code from Byte Technical Interview Prep w/ A - 4/28/2020 @ 6PM
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # case 0: both are empty
        # case 1: l1 is empty
        # case 2: l2 is empty
        # case 3: both non-empty, l1[0] < l2[0]
        # case 4: both non-empty, l1[0] < l2[0]
        l3 = ListNode('Head')
        tail = l3
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return l3.next

# Success - Details 
# Runtime: 20 ms, faster than 99.97% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.9 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.

# Runtime: 40 ms, faster than 35.94% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.1 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.



'''