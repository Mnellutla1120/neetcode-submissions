# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
         if not preorder or not inorder:
             return None

         root = TreeNode(preorder[0])
         mid = inorder.index(preorder[0])
         # preorder from 1 to mid (we start at root which is idx = 0)
         # the inorder version of that will just be starting from left side all the way to mid
         root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # preorder from mid+1 to end for right (build right subtree)
         # the inorder version of that will just be starting from mid+1 all the way to right leaf, since we alr take mid into account on left
         root.right = self.buildTree(preorder[mid + 1:], inorder[mid+1:])
         return root


        