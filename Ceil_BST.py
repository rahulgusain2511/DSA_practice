
'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def findCeil(node, x):
    ans = -1

    while node:
        if node.data < x:
            node = node.right
        else:
            ans = node.data
            node = node.left

    return ans