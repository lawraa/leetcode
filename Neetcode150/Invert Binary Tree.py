from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        from collections import deque
        q = deque([root])
        
        while q:
            curr_node = q.popleft()
            if curr_node.left or curr_node.right:
                curr_node.left, curr_node.right = curr_node.right, curr_node.left
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)

        return root

# time complexity: O(n)
# space complexity: O(n)