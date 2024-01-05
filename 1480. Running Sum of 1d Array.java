class Solution {
    public int[] runningSum(int[] nums) {
        int [] arr = new int [nums.length];
        int sum = 0;
        for(int i=0;i<nums.length;i++){
            arr[i] = sum + nums[i];
            sum = arr[i];
        }
        return arr;
    }
}




// below is the cpp code as well 
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        int sum = 0;
        for(int i=0;i<n;i++){
            ans[i] = sum + nums[i];
            sum = ans[i];
        }
        return ans;
    }
};
