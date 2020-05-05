# 142. Linked List Cycle II
# Difficulty - Medium
# https://leetcode.com/problems/linked-list-cycle-ii/

# Given a linked list, return the node where the cycle begins. If there is no 
# cycle, return null.
# To represent a cycle in the given linked list, we use an integer pos which 
# represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.

# My Note: the explantion has an image that represents it but the image
# cannot be seen here, go to the link 

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# Example 2:
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.

# Example 3:
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#Tortise and Hare Algorithm

def detectCycle(head):
    if not head:
        return None
    tortise = hare = head
    while hare and hare.next:
        tortise, hare = tortise.next, hare.next.next
        if tortise == hare:
            while head != tortise:
                head, tortise = head.next, tortise.next
            return head
    return None

# Success - Details: 
# Runtime: 48 ms, faster than 81.01% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.

# Runtime: 48 ms, faster than 81.01% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.

# Runtime: 48 ms, faster than 81.01% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 17 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.

'''
# "Naive Approach" - My Initial Soution
def detectCycle(head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return None
    
    node_dict = {}
    pos = 0
    node_dict[head] = pos
    current = head
    while current.next:
        current = current.next
        pos += 1
        
        if current not in node_dict.keys():
            node_dict[current] = pos
        else:
            return current
    return None

# Success - Details 

# Runtime: 48 ms, faster than 80.34% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 17 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II

# Runtime: 52 ms, faster than 56.33% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.

# Runtime: 52 ms, faster than 56.33% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.

# Runtime: 52 ms, faster than 56.33% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 16.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.
'''



# '''
e1 = ListNode(3)
e2 = ListNode(2)
e1.next = e2
e3 = ListNode(0)
e2.next = e3
e4 = ListNode(-4)
e3.next = e4
e4.next = e2
# e1 --> e2 --> e3 --> e4 --> back to e2 
# '''

'''
e1 = ListNode(1)
e2 = ListNode(2)
e1.next = e2
e2.next = e1
# e1 --> e2 --> back to e1 
'''

'''
e1 = ListNode(1)
# e1 --> None 
'''

result = detectCycle(e1)
print(None) if result == None else print(result.val)