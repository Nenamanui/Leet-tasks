# Time:   O(n)
# Space:  O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, max_v, min_v):
            if node is None:
                return True

            if node.val <= min_v or node.val >= max_v:
                return False

            if not check(node.left, node.val, min_v):
                return False
            if not check(node.right, max_v, node.val):
                return False

            return True
        return check(root, 2**32, -2**32)