public class Solution {
    // Paste your final solution here.

	public static int candy(int[] ratings){
		int n = ratings.length;

		int[] left = new int[n];
		left[0] = 1;
		for(int i = 1 ; i < n ; ++i){
			if(ratings[i] > ratings[i-1]){
				left[i] = left[i-1] + 1;
			}
			else{
				left[i] = 1;
			}
		}

		int curr = 1, right = 1;
		int sum = Math.max(left[n-1], 1);
		for(int i = n-2 ; i >= 0 ; --i){
			if(ratings[i] > ratings[i+1]){
				curr = right + 1;
			}
			else{
				curr = 1;
			}
			right = curr;
			sum += Math.max(left[i], curr);
		}
		return sum;
	}
    
    // You can write a main() to test locally; LeetCode ignores it.
    public static void main(String[] args) {
        // quick local check
        System.out.println("Ready to code: Solution");
    }
}
