from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        dummy = Node(x = 0, next = head)
        new_head = Node(x = head.val)
        dummy_new = Node(x = 0, next = new_head)

        from collections import defaultdict
        
        record = defaultdict(Node)

        record[head] = new_head
        while head.next:
            new_head.next = Node(x = head.next.val)
            head = head.next
            new_head = new_head.next
            record[head] = new_head
        new_head.next = None

        head = dummy.next
        new_head = dummy_new.next
        while head:
            if head.random == None:
                new_head.random = None
            else:
                new_head.random = record[head.random]
            new_head = new_head.next
            head = head.next

        return dummy_new.next

# Time complexity: O(n)
# Space complexity: O(n)

        