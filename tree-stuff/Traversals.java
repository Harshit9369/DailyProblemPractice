import java.util.*;

class Node{
	int data;
	Node left;
	Node right;

	Node(int key){
		this.data = key;
		this.left = null;
		this.right = null;
	}
	
}

public class Traversals{

	public static void inorder(Node root){
		if(root == null){
			return;
		}
		inorder(root.left);
		System.out.print(root.data + " ");
		inorder(root.right);
	}

	public static void preorder(Node root){
		if(root == null){
			return;
		}
		System.out.print(root.data + " ");
		preorder(root.left);
		preorder(root.right);
	}

	public static void postorder(Node root){
		if(root == null){
			return;
		}
		postorder(root.left);
		postorder(root.right);
		System.out.print(root.data + " ");
	}

	public static void levelorder(Node root){
		if(root == null) return;
		Queue<Node> q = new LinkedList<>();
		q.add(root);

		while(!q.isEmpty()){
			int size = q.size();
			for(int i = 0 ; i < size ; ++i){
				Node curr = q.peek();
				if(curr.left != null) q.offer(curr.left);
				if(curr.right != null) q.offer(curr.right);
				System.out.print(q.poll().data + " ");
			}
		}
		System.out.println();
	}

	public static void main(String[] args){
		Node root = new Node(1);
		root.left = new Node(2);
		root.right = new Node(3);
		root.left.left = new Node(4);
		root.left.right = new Node(5);
		root.right.right = new Node(6);

		inorder(root);
		System.out.println();
		preorder(root);
		System.out.println();
		postorder(root);
		System.out.println();
		levelorder(root);
	}
}
