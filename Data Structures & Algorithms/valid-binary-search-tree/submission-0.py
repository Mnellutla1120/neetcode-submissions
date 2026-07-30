# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
          curr = root
          if curr.val > curr.left.val and curr.val < curr.right.val:
             return True
          else:
             return False    
          return self.isValidBST(self,root.left) and self.isValidBST(self,root.right)

          

        