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
    public List<Integer> preorderTraversal(TreeNode root) {
        
        List<Integer> ans = new ArrayList<>();

        if(root == null) return ans;

        Stack<TreeNode> st = new Stack<>();

        TreeNode curr = root;
        st.push(curr);

        while(!st.isEmpty()){
            TreeNode a = st.peek();
            ans.add(a.val);
            st.pop();
            if(a.right != null){
                st.push(a.right);
            }
            if(a.left != null){
                st.push(a.left);
            }
        }
        return ans;
    }
}




// below is the recurssive code 

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

    public void dfs(List<Integer> ans , TreeNode root){

       //  List<Integer> preOrder = new ArrayList<>(); 
        if(root == null ) return ;

        ans.add(root.val);
        dfs(ans, root.left);
        dfs(ans, root.right);

    }


    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> preOrder = new ArrayList<>();

        dfs(preOrder, root);

        return preOrder;
    }
}
