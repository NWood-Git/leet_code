# Recursion Card Chapter 1 - 24. Swap Nodes in Pairs - 5/13-14/2020 
# Difficulty: Medium
# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        old_head = head
        new_head = head.next
        recursive_result = self.swapPairs(new_head.next)
        new_head.next = old_head
        old_head.next = recursive_result
        return new_head


# Submission Detail
# 55 / 55 test cases passed.
# Status: Accepted
# Runtime: 28 ms / 32 ms
# Memory Usage: 13.8 MB / 14 MB
# Your runtime beats 78.07 % / 50.94 % of python3 submissions.