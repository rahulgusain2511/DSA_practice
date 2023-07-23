# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        if root==None:
            return TreeNode(val)
        curr=root
        while True:
            if curr.val<val:
                if curr.right==None:
                    curr.right=TreeNode(val)
                    break
                curr=curr.right
            else:
                if curr.left==None:
                    curr.left=TreeNode(val)
                    break
                curr=curr.left
        return root
