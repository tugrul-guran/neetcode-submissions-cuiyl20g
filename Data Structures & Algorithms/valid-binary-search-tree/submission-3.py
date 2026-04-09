# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _validate(self, node: Optional[TreeNode], left_bound: int, right_bound: int) -> bool:
        if node is None:
            return True

        if node.val <= left_bound or node.val >= right_bound:
            return False

        return self._validate(node.left, left_bound, node.val) and self._validate(node.right, node.val, right_bound)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self._validate(root, -1001, 1001)