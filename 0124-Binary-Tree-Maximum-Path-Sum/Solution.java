class TreeNode{
	int data;
	TreeNode left;
	TreeNode right;

	TreeNode(int key){
		this.data = key;
		this.left = null;
		this.right = null;
	}
}

public class Solution {

	static int max = Integer.MIN_VALUE;
    public static int maxPathSum(TreeNode root){
    	max = root.val;
    	maxSum(root);
    	return max;
    }

    public static int maxSum(TreeNode root){
    	if(root == null) return 0;

    	int lsum = Math.max(0, maxSum(root.left));
    	int rsum = Math.max(0, maxSum(root.right));
    	max = Math.max(root.val + lsum + rsum, Math.max(root.val + lsum, root.val + rsum));
    	return root.val + Math.max(lsum, rsum);
    }
}
