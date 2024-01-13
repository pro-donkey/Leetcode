class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length;
        int a = 0;
        int b = 0;
        int c = 0;

        for(Integer i : nums){
            if(i == 0) a ++;
            else if(i == 1) b ++;
            else c ++;
        }
        int indx = 0;
        while(a > 0){
            nums[indx] = 0;
            indx++;
            a--;
        }
        while(b > 0){
            nums[indx] = 1;
            indx++;
            b--;
        }
        while(c > 0){
            nums[indx] = 2;
            indx++;
            c --;
        }
    }
}
