
# Definition for a binary tree node.

class Solution:
    def isValidBST(self, root: Treenode) -> bool:
        def helper(node, lower, upper):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root, float('-inf'), float('inf'))
        