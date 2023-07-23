# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        def right(root,level):
            if root is None:
                return 
            if level==len(s):
                s.append(root.val)
            right(root.right,level+1)
            right(root.left,level+1)
        if root is None:
            return []
        else:
            s=[]
            right(root,0)
            return s
