class Solution:
    def deleteNode(self, root,key):
        
        if not root:
            return None
        

        if key < root.val:
            root.left = self.deleteNode(root.left, key)


        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:

            if not root.left:
                return root.right
            
            elif not root.right:
                return root.left
            
            else:

                node = root.right
                
                while node.left:

                    node = node.left
               
                root.val = node.val

                root.right = self.deleteNode(root.right, node.val)
        
        return root