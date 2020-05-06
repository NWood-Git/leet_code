# 23. Merge k Sorted Lists
# Difficulty - Hard
# https://leetcode.com/problems/merge-k-sorted-lists/

# Done in Technical Interview Prep w/ Anton / Byte

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # counting sort
        nodes_at_value = {}
        min_val = max_val = None
        for head_node in lists:
            while head_node:
                value = head_node.val
                nodes = nodes_at_value.get(value, [])
                nodes.append(head_node)
                nodes_at_value[value] = nodes
                min_val = min(min_val, value) if min_val != None else value
                max_val = max(max_val, value) if max_val != None else value
                head_node = head_node.next
        head = tail = ListNode('dummy')
        if min_val == None:
            return None
        for value in range(min_val, max_val + 1):
            if value in nodes_at_value:
                nodes = nodes_at_value[value]
                for node in nodes:
                    tail.next = node
                    tail = node
        return head.next

# Submission Detail
# 131 / 131 test cases passed.
# Status: Accepted
# Runtime: 100 ms
# Memory Usage: 17.1 MB
# Your runtime beats 85.55 % of python3 submissions.
