# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution(object):
    def isValidBST(self, root):
        m1,m2=-sys.maxsize,sys.maxsize
        def check(root,m1,m2):
            if root==None:
                return True
            if root.val<=m1 or root.val>=m2:
                return False
            return check(root.left,m1,root.val) and check(root.right,root.val,m2)
        return check(root,m1,m2)
