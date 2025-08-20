public class Solution2 {
    public int candy(int[] ratings) {
        int n = ratings.length;
        if (n == 1) return 1;

        int sum = 1;

        int i = 1;
        while(i < n){
            if(ratings[i] == ratings[i-1]){
                sum++;
                i++;
                continue;
            }
            int peak = 1;
            while(i < n && ratings[i] > ratings[i-1]){
                peak += 1;
                sum += peak;
                i++;
            }
            int down = 1;
            while(i < n && ratings[i] < ratings[i-1]){
                sum += down;
                down++;
                i++;
            }
            if(down > peak) sum += down - peak;
        }
        
        return sum;

    }
}
