class Solution {
    public int returnToBoundaryCount(int[] nums) {
        int cnt = 0;
        int ans = 0;
        for(Integer it : nums){
            ans += it;
            
            if(ans == 0) cnt += 1;
            
        }
        return cnt;
    }
}
