/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        else {
            return isValid(root,LONG_MIN,LONG_MAX);
        }
   

        
    }
        bool isValid(TreeNode* root, long low, long high) {

          if (root == nullptr) {
            return true;
          }
         if (!(low < root->val && high > root->val)) {
            return false;
         }
         else {
        return isValid(root->left,low,root->val) && isValid(root->right,root->val,high);
         }

    }


};
