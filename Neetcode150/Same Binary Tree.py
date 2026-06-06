from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (not p and q) or (not q and p):
            return False 
            
        if p.val != q.val:
            return False

        from collections import deque

        p_q = deque([p])
        q_q = deque([q])

        while p_q:
            curr_p = p_q.popleft()
            curr_q = q_q.popleft()

            if curr_p.val != curr_q.val:
                return False
            
            if curr_p.left and curr_q.left:
                p_q.append(curr_p.left)
                q_q.append(curr_q.left)
            elif (curr_p.left and not curr_q.left) or (curr_q.left and not curr_p.left):
                return False   

            if curr_p.right and curr_q.right:
                p_q.append(curr_p.right)
                q_q.append(curr_q.right)
            elif (curr_p.right and not curr_q.right) or (curr_q.right and not curr_p.right):
                return False  

        return True
    

    # Optimal solution for exampe: 
    # from collections import deque

    # class Solution:
    #     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #         queue = deque([(p, q)])

    #         while queue:
    #             node1, node2 = queue.popleft()

    #             if not node1 and not node2:
    #                 continue

    #             if not node1 or not node2:
    #                 return False

    #             if node1.val != node2.val:
    #                 return False

    #             queue.append((node1.left, node2.left))
    #             queue.append((node1.right, node2.right))

    #         return True

# Time complexity: O(n)
# Space complexity: O(n)
