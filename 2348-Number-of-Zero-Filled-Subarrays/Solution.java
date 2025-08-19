public class Solution {
    public long zeroFilledSubarray(int[] nums) {
        int n = nums.length;
        long ans = 0;
        long cnt = 0;
        for(int i = 0 ; i < n ; ++i){
            if(nums[i] != 0){
                ans += (cnt * (cnt + 1)) / 2;
                cnt = 0;
            }
            else{
                cnt++;
                if(i == n-1){
                    ans += (cnt * (cnt + 1)) / 2;
                }
            }
        }
        return ans;
    }
}
