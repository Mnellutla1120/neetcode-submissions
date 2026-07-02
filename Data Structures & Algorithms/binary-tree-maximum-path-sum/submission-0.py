# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] #start w root

    #make a helper dfs function
        def dfs(root):
            if not root:
                 return 0 #tree is empty, max path is 0
            #compute path w/o split
            l_max = dfs(root.left)
            r_max = dfs(root.right)
            l_max = max(l_max,0) #from start of left subtree to leaf
            r_max = max(r_max,0) #from start of right subtree to leaf
            #max path w/ split
            res[0] = max(res[0], root.val + l_max + r_max)
            
      #return max path w/0 split 
            return root.val + max(l_max, r_max)

        dfs(root)
        return res[0]

       

