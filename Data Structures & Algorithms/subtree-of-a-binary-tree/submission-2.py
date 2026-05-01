# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        
        #empty tree alway subtrr
        if not subRoot:
            return True
        
        #base case  
        if not root:
            return False


 
        #check at every node
        if self.isTheSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isTheSame(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val != subRoot.val:
            return False
        return self.isTheSame(root.left, subRoot.left) and self.isTheSame(root.right, subRoot.right)

    
        