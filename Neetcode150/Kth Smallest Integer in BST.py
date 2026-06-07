from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # from least to most in bst, we need to do inorder
        # which is left -> mid -> right
        self.rank = 0
        self.res = None

        def dfs(node):
            if not node or self.res is not None:
                return

            dfs(node.left)
            self.rank += 1
            if self.rank == k:
                self.res = node.val
                return
            dfs(node.right)

        dfs(root)
        return self.res

# Time complexity: O(n)
# Space complexity: O(n)