# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # use stack that stores small,smaller,bigger than small, so on so forth and pop accordingly

        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr) #process nodes onto stack
                curr = curr.left
            curr = stack.pop() #pop accordingly
            k -= 1
            if k == 0:
                 return curr.val
            curr = curr.right #go right since we are now looking for biggest element
        