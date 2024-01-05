class Solution {
    public int[] leftRightDifference(int[] nums) {
       int n = nums.length;
       int [] pre = new int[n];
       int [] suf = new int[n];
       pre[0] = 0; suf[n-1] = 0;
       for(int i=1;i<n;i++){
           pre[i] = pre[i-1] + nums[i-1];
       } 
       for(int i=n-2;i>-1;i--){
           suf[i] = suf[i+1] + nums[i+1];
       }

       for(int i=0;i<n;i++){
           pre[i] = Math.abs(pre[i] - suf[i]);
       }
       return pre;
    }
}
