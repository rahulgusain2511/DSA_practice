# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while len(q):
            lev = []
            for i in range(len(q)):
                el = q.popleft()
                lev.append(el.val)
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
            res.append(lev)      
        return res