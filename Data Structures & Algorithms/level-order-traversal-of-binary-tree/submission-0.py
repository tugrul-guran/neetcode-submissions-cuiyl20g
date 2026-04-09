# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        else:
            result = []

            queue = [[root]]
            while queue:
                items = queue.pop()
                result.append([i.val for i in items])

                subtrees = []
                for tree in items:
                    l, r = tree.left, tree.right

                    if l is not None:
                        subtrees.append(l)

                    if r is not None:
                        subtrees.append(r)
                
                if subtrees:
                    queue.append(subtrees)

            return result