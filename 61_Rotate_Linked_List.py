# 61. Rotate List
# Difficulty - Medium
# https://leetcode.com/problems/rotate-list/


# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Example 1: Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL

# Example 2: Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL





# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print_ll(self):
        current = self
        print(current.val, end= ' -> ')
        while current.next:
            current = current.next
            print(current.val, end= ' -> ')
        print()

def rotateRight( head: ListNode, k: int) -> ListNode:
    if head == None or head.next == None:
        return head

    len_ll = 1
    current = head
    while current.next:
        current = current.next
        len_ll +=1
    
    if k == len_ll or k == 0 or k % len_ll ==0:
        return head
    elif k >len_ll:
        k = k % len_ll
    
    split_after = len_ll - k
    current = head
    for i in range(split_after - 1):
        current = current.next
    new_head = current.next
    current.next = None
    
    new_curr = new_head
    while new_curr.next:
        new_curr = new_curr.next
    new_curr.next = head
    
    return new_head

# Success - Details 
# Runtime: 44 ms, faster than 16.02% of Python3 online submissions for Rotate List.
# Memory Usage: 13.9 MB, less than 6.45% of Python3 online submissions for Rotate List.

# Runtime: 32 ms, faster than 87.74% of Python3 online submissions for Rotate List.
# Memory Usage: 14 MB, less than 6.45% of Python3 online submissions for Rotate List.

# Runtime: 28 ms, faster than 96.68% of Python3 online submissions for Rotate List.
# Memory Usage: 13.7 MB, less than 6.45% of Python3 online submissions for Rotate List.

e1 = ListNode(1)
e2 = ListNode(2)
e1.next = e2
e3 = ListNode(3)
e2.next = e3
e4 = ListNode(4)
e3.next = e4
e5 = ListNode(5)
e4.next = e5

e1.print_ll()
rotated_e1 = rotateRight(e1, 12)
rotated_e1.print_ll()