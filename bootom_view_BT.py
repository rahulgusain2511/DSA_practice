
from collections import deque
class Solution:
    def bottomView(self, root):
        queue=deque()
        queue.append([root,0])
        d=dict()
        while queue:
            node,level=queue.popleft()
            d[level]=node.data
            if node.left:
                queue.append([node.left,level-1])
            if node.right:
                queue.append([node.right,level+1])
        ans=[d[i] for i in sorted(d.keys())]
        return ans