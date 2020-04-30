# 206. Reverse Linked List - Sovled 4/29-30/2020
# Difficulty - Easy
# https://leetcode.com/problems/reverse-linked-list/

# Description:
# Reverse a singly linked list.

# Example: Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.


# Solution from thecodingworld youtube: https://www.youtube.com/watch?v=gSs3U18v4xE

# 1 Set previous as None, Current as head, and next as none
# 2 Iterate until current is None
# 3 Set mext mpde pf current to previous
# 4 Set previous as current, current as next and next as it's next node
# 5 set the head pointer to the previous Node

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head = prev
        return head

# Success - Details 
# Runtime: 36 ms, faster than 59.65% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.4 MB, less than 25.00% of Python3 online submissions for Reverse Linked List.

# Runtime: 36 ms, faster than 59.65% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.4 MB, less than 25.00% of Python3 online submissions for Reverse Linked List.




# Same as below but this is all that is needed for leetcode
# In this attempt i created a doubly linked list then made the head and next 
# match the reverse version
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        current = head
        current.prev = None
        while current.next:
            current.next.prev = current
            current = current.next
        self.tail = current
        # print("Now Reverse")
        while current:
            current.next = current.prev
            current = current.prev
        self.head = self.tail
        return self.head

# Success - Details 
# Runtime: 32 ms, faster than 83.38% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.2 MB, less than 31.82% of Python3 online submissions for Reverse Linked List.

# Runtime: 36 ms, faster than 59.65% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.4 MB, less than 25.00% of Python3 online submissions for Reverse Linked List.

# Runtime: 40 ms, faster than 27.84% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.3 MB, less than 26.14% of Python3 online submissions for Reverse Linked List.

'''

#change prev to temp 

class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev #added line

class LinkedList:
    def __init__(self, head=None, tail= None):
        self.head = head
        self.tail = None

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
            # self.tail = current.next
        else:
            self.head = new_element
            # self.tail = new_element
            
    # def length_ll(self):
    #     current = self.head
    #     count = 1
    #     while current.next:
    #         current = current.next
    #         count += 1
    #     return count

    # def reverseList(self, head: ListNode) -> ListNode:
    #     current = head
    #     print(current.val)
    #     while current.next:
    #         current.next.prev = current
    #         current = current.next
    #         print(current.val)
    #     self.tail = current
    #     print("Now Reverse")
    #     print(current.val)
    #     while current != self.head:
    #         current = current.prev
    #         print(current.val)

    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        current.prev = None
        while current.next:
            current.next.prev = current
            current = current.next
        self.tail = current
        # print("Now Reverse")
        while current:
            current.next = current.prev
            current = current.prev
        self.head = self.tail
        

    def print_ll_rev(self):
        current = self.tail
        print(current.val, end = ' -> ')
        while current != self.head:
            current = current.prev
            print(current.val, end = ' -> ')
        print()

    def print_ll(self):
        current = self.head
        print(current.val, end = ' -> ')
        while current.next:
            current = current.next
            print(current.val, end = ' -> ')
        print()


e1 = ListNode(1)
e2 = ListNode(2)
e3 = ListNode(3)
e4 = ListNode(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)

ll.print_ll()
print()
ll.reverseList(e1)
print()
# ll.print_ll_rev()
ll.print_ll()
print()

# current = ll.tail
# while current.prev:
#     current = current.prev
# print(current.val)