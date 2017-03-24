"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # write your code here
        
        paths = []
        if root == None:
            return paths
            
        if root.left == None and root.right == None:
            paths.append("" + root.val)
            return paths
        
        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)
        
        for path in leftPaths:
            paths.append(root.val + "->" + path)
            
        for paths in rightPaths:
            paths.append(root.val + "->" + path)
            
        return paths