from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            return None
        res = head
        curr_n = n
        before_remove_node = head
        remove_node = head
        while head.next:
            head = head.next
            curr_n -= 1
            if curr_n < 0:
                before_remove_node = before_remove_node.next

            if curr_n < 1:
                remove_node = remove_node.next

        if remove_node == before_remove_node:
            res = remove_node.next
        else:
            temp = before_remove_node.next    
            before_remove_node.next = before_remove_node.next.next
            temp.next = None

        return res

# Time complexity: O(n)
# Space complexity: O(1)