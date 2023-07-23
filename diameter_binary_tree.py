# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 0  # variable to store the maximum diameter found so far
        
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            self.ans = max(self.ans, left + right)  
            return max(left, right) + 1  
            
        height(root)
        return self.ans
       