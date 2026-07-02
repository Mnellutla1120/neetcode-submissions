# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #if node bigger than root, move left, if node smaller, move right and keep going recursively
         if not root:
            return None
         #swap
         root.left, root.right = root.right, root.left

         self.invertTree(root.left)
         self.invertTree(root.right)
         return root



        


      
        