import java.util.*;

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

	static int max = 0;
    public static int maxDepth(TreeNode root){
    	height(root);
    	return max;
    }

    public static int height(TreeNode root){
    	if(root == null) return 0;
    	return 1 + Math.max(height(root.left), height(root.right));
    }
}
