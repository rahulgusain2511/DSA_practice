'''
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''
import sys
def minVal(root):
    ans = sys.maxsize

    if root is None:
        return -1

    while root is not None:
        ans = min(ans, root.data)
        root = root.left

    return ans