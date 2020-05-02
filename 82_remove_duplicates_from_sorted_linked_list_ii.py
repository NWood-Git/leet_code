# 82. Remove Duplicates from Sorted List II
# Difficulty - Medium
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Description:
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Return the linked list sorted as well.

# Example 1: Input: 1->2->3->3->4->4->5
# Output: 1->2->5

# Example 2: Input: 1->1->1->2->3
# Output: 2->3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print_ll(self):
        current = self
        print(current.val, end = ' -> ')
        while current.next:
            current = current.next
            print(current.val, end = ' -> ')
        print()




def deleteDuplicates(head: ListNode) -> ListNode:
    prev = current =  head
    val_set = set()

    if head == None:
        return None
    if head.next == None:
        return head
    elif head.next.next == None:
        return head if head.val != head.next.val else None

    while current.next:
        if current == head:
            if current.val == current.next.val or current.val in val_set:
                val_set.add(current.val)
                prev = head = current.next
        else:
            if current.val == current.next.val or current.val in val_set:
                val_set.add(current.val)
                prev.next = current.next
            else:
                prev = current
        current = current.next

    # if current.val == head.val and head,val in val_set:
    if current.val in val_set:
        prev.next = None
    if head.val in val_set:
        return None
    # print(val_set)
    return head
# 
# Success - Details 
# Runtime: 32 ms, faster than 97.45% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 13.8 MB, less than 8.00% of Python3 online submissions for Remove Duplicates from Sorted List II.

# Runtime: 40 ms, faster than 67.47% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 13.9 MB, less than 8.00% of Python3 online submissions for Remove Duplicates from Sorted List II.

# Runtime: 52 ms, faster than 8.22% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 13.8 MB, less than 8.00% of Python3 online submissions for Remove Duplicates from Sorted List II.

# Runtime: 60 ms, faster than 6.15% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 14.1 MB, less than 8.00% of Python3 online submissions for Remove Duplicates from Sorted List II.

# Runtime: 76 ms, faster than 5.54% of Python3 online submissions for Remove Duplicates from Sorted List II.
# Memory Usage: 13.8 MB, less than 8.00% of Python3 online submissions for Remove Duplicates from Sorted List II.

'''
e0 = ListNode(1)
e1 = ListNode(1)
e0.next = e1
e2 = ListNode(2)
e1.next = e2
e3 = ListNode(3)
e2.next = e3
e4 = ListNode(3)
e3.next = e4
e5 = ListNode(4)
e4.next = e5
e6 = ListNode(4)
e5.next = e6
e7 = ListNode(5)
e6.next = e7

e0.print_ll()
new = deleteDuplicates(e0)
new.print_ll()

# print(e0)
# print(e1)
# print(new)
'''

'''
e0 = ListNode(1)
e1 = ListNode(2)
e0.next = e1
e2 = ListNode(2)
e1.next = e2

e0.print_ll()
new = deleteDuplicates(e0)
new.print_ll()
'''
'''
e0 = ListNode(1)
e1 = ListNode(1)
e0.next = e1
e2 = ListNode(1)
e1.next = e2

e0.print_ll()
new = deleteDuplicates(e0)
new.print_ll()
'''