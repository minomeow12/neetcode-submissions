# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        #delete
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                ios_node = self.find_ios(root.right)
                root.val = ios_node.val
                root.right = self.deleteNode(root.right, ios_node.val)
        return root

    def find_ios(self, node):
        if node.left is None:
            return node
        return self.find_ios(node.left)

        

        
