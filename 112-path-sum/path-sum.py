# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val==targetSum
        l=self.hasPathSum(root.left,targetSum-root.val)
        r=self.hasPathSum(root.right,targetSum-root.val)
        return l or r
