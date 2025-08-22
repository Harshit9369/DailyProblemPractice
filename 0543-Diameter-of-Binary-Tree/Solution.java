class TreeNode{
	int data;
	TreeNode left;
	TreeNode right;

	public TreeNode(int key){
		this.data = key;
		this.left = null;
		this.right = null;
	}
}

public class Solution {

	static int maxi = 0;
	public static int diameter(TreeNode root){
		height(root);
		return maxi;
	}

	public static int height(TreeNode root){
		if(root == null) return 0;

		int lh = height(root.left);
		int rh = height(root.right);
		maxi = Math.max(maxi, lh + rh);
		return 1 + Math.max(lh, rh);
	}
    
}
