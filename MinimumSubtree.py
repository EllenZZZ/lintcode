"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the minimum subtree
    
    import sys
    minimum_weight = sys.maxint
    res = None
    
    def findSubtree(self, root):
        # Write your code here
        
        self.recursion(root)
        return self.res
        
    def recursion(self, root):
        if root is None:
            return 0
        
        left_weight = self.recursion(root.left)
        right_weight = self.recursion(root.right)
        
        sum = left_weight + right_weight + root.val
        if sum <= self.minimum_weight:
            self.minimum_weight = sum
            self.res = root
        
        return sum

