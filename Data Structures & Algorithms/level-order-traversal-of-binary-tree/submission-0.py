  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        h = self.height(root)
        arr = [[] for _ in range(h)]

        queue = deque()
        queue.append(root)
        level = -1
        while len(queue) > 0:  
            level += 1
            for i in range(len(queue)):
                curr = queue.popleft()
                arr[level].append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return arr

        
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


        
        


        
        