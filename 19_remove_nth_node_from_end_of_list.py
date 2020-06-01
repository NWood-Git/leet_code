# 19. Remove Nth Node From End of List
# Difficulty - Medium
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    current = head
    ll_dict = {}
    counter = 1
    while current:
        ll_dict[counter] = current
        counter += 1
        current = current.next
    counter -= 1
    if counter == n:
        if n == counter == 1:
            return None
        else:
            head = head.next
    elif n >= 2:
        prev_node = ll_dict[counter-n]
        prev_node.next = ll_dict[counter-n +2]
    elif n == 1:
        prev_node = ll_dict[counter-n]
        prev_node.next = None
    return head

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(3)
node2.next = node3
node4 = ListNode(4)
node3.next = node4
node5 = ListNode(5)
node4.next = node5

removeNthFromEnd(node1, 2)
current = node1
while current:
    print(current.val)
    current = current.next

# Success Details: 
# Runtime: 28 ms, faster than 88.30% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.6 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.

# Runtime: 20 ms, faster than 99.50% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.9 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.

# Runtime: 28 ms, faster than 88.30% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.7 MB, less than 6.06% of Python3 online submissions for Remove Nth Node From End of List.