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


public class IterativeTraversals{

	public static void iterativePreorder(Node root){
		if(root == null) return;
		Stack<Node> st = new Stack<>();
		st.push(root);

		while(!st.isEmpty()){
			Node curr = st.pop();
			System.out.print(curr.data + " ");
			if(curr.right != null) st.push(curr.right);
			if(curr.left != null) st.push(curr.left);
		}

		System.out.println();
	}

	public static void iterativePostorder(Node root){
		if(root == null) return;
		Node curr = root;
		Stack<Node> st = new Stack<>();
		// st.push(curr);
		while(curr != null || !st.isEmpty()){
			if(curr != null){
				st.push(curr);
				curr = curr.left;
			}
			else{
				Node temp = st.peek().right;
				if(temp == null){
					temp = st.pop();
					System.out.print(temp.data + " ");
					while(!st.isEmpty() && temp == st.peek().right){
						temp = st.pop();
						System.out.print(temp.data + " ");
					}
				}
				else{
					curr = temp;
				}
			}
			
		}
		System.out.println();
	}

	public static void iterativePostorderTwo(Node root){
		if(root == null) return;
		Stack<Node> st1 = new Stack<>();
		Stack<Node> st2 = new Stack<>();

		st1.push(root);
		while(!st1.isEmpty()){
			Node curr = st1.pop();
			if(curr.left != null){
				st1.push(curr.left);
			}
			if(curr.right != null){
				st1.push(curr.right);
			}
			st2.push(curr);
		}
		while(!st2.isEmpty()){
			System.out.print(st2.pop().data + " ");
		}
		System.out.println();
	}

	public static void iterativeInorder(Node head){
		Node node = head;

		Stack<Node> st = new Stack<>();

		while(true){
			if(node != null){
				st.push(node);
				node = node.left;
			}
			else{
				if(st.isEmpty()) break;
				node = st.pop();
				System.out.print(node.data + " ");
				node = node.right;
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

		iterativePreorder(root);
		iterativeInorder(root);
		iterativePostorderTwo(root);
		iterativePostorder(root);
	}
}
