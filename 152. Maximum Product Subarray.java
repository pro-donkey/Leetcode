
// using kadanes algo 
// very important 


class Solution {
    public int maxProduct(int[] nums) {
        int prod = 1;
        int mx = Integer.MIN_VALUE;
        for(int i=0;i<nums.length;i++){
            prod *= nums[i];
            mx = Math.max(mx,prod);
            if(prod == 0){
                prod = 1;
            }
        }
        prod = 1;
        for(int i=nums.length-1;i>-1;i--){
            prod *= nums[i];
            mx = Math.max(mx,prod);
            if(prod == 0){
                prod = 1;
            }
        }
        return mx;
    }
}
