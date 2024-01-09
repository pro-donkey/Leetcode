class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cnt = 0;
        int mx = 0;
        for(int i=0;i<nums.length;i++){
            if(nums[i] == 1){
                cnt += 1;
                mx  = Math.max(mx,cnt);
            }
            else {
                cnt = 0;
            }
        }
        return mx;
    }
}
