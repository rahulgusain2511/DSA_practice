# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        d=[]

        def inOrder(root):
            if root is not None:
                d.append(root.val)
                inOrder(root.left)
                inOrder(root.right)
        
        inOrder(root)

        for i in range(len(d)-1):
            a=d[i]
            for j in range(i+1,len(d)):
              b=d[j]
              if a+b == k:
                  return True 
        return  False 
