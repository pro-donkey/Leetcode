/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private void  dfs(List<Integer> ans, TreeNode root){
        if(root == null ) return ;

        dfs(ans, root.left);
        dfs(ans,root.right);
        ans.add(root.val);

    }
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> postOrder = new ArrayList<Integer> ();

        dfs(postOrder, root);
        return postOrder;
    }
}
