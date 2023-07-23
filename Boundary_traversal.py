class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def LeftBoundary(root):
    if root==None or (root.left==None and root.right==None):
        return
    if root.left:
        res.append(root.data)
        LeftBoundary(root.left)
    else:
        res.append(root.data)
        LeftBoundary(root.right)

def Leaves(root):
    if root==None:
        return
    if root.left==None and root.right==None:
        res.append(root.data)
    Leaves(root.left)
    Leaves(root.right)

def RightBoundary(root):
    if root==None or (root.left==None and root.right==None):
        return 
    if root.right:
        RightBoundary(root.right)
        res.append(root.data)
    else:
        RightBoundary(root.left)
        res.append(root.data)
def traverseBoundary(root):
    # Write your code here.
    global res
    res=[]
    if root==None:
        return res
    res.append(root.data)
    LeftBoundary(root.left)
    Leaves(root.left)
    Leaves(root.right)
    RightBoundary(root.right)
    return res