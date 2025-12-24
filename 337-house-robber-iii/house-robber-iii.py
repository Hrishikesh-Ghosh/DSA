# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(root):
            if not root:
                return [0,0]
            LeftNode = dfs(root.left)
            RightNode = dfs(root.right)
            withRoot = root.val + LeftNode[1] + RightNode[1]
            withoutRoot = max(LeftNode) + max(RightNode)
            return (withRoot, withoutRoot)
        return max(dfs(root))