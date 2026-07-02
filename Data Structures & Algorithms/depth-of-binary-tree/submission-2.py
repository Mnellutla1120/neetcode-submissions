# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #optimized solution
        #preorder traversal starting from the root
        stack = [[root,1]] #we add our root of depth 1
        res = 0
        while stack:
             node,depth = stack.pop() #we process our nodes accordingly by popping LAFO

             if node:
                 res = max(res,depth)
                 stack.append([node.left,depth+1])
                 stack.append([node.right,depth+1])
        return res

     



        