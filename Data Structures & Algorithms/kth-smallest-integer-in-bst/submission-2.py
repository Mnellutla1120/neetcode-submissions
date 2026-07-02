# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 #start with our index to get to k
        stack = []
        curr = root

        while stack or curr: #while one of them is unempty
             while curr:
                stack.append(curr)
                curr = curr.left #keep going to our leftmost node
             curr = stack.pop() #process our nodes
             n += 1
             if n == k: #we found it!
                 return curr.val
             curr = curr.right #if we didn't find it, we recurse right and look for the kth smallest element there




            
