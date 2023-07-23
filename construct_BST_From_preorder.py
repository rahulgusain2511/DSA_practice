#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import sys
class Solution:
    def bstFromPreorder(self, A):
        index = [0]  # Using a list to store the index, as integers are immutable in Python

        def build(bound):
            if index[0] == len(A) or A[index[0]] > bound:
                return None
            root = TreeNode(A[index[0]])
            index[0] += 1
            root.left = build(root.val)
            root.right = build(bound)
            return root

        return build(sys.maxsize)