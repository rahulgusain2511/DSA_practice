# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        ans = []
        if not root:
            return None
        q = deque([root])
        level_index = 1
        while(q):
            n = len(q)
            level = []
            for i in range(0,n):
                node = q.popleft()
                level.append(node.val)
                if (node.left != None):
                    q.append(node.left)
                if (node.right != None):
                    q.append(node.right)
            if (level_index%2==0):
                level.reverse()
                ans.append(level[:])
            else:
                ans.append(level[:])
            level_index+=1
        return ans