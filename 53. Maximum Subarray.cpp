class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // Kadanes Algorithm
        int sum = 0;
        int maxi = INT_MIN;
        for(int i=0;i<nums.size();i++){
            sum += nums[i];
            if(sum > maxi){
                maxi = sum;
            }
            if(sum < 0){
                sum = 0;
            }
        }
        return maxi;
    }
};

// This code is solved using Kadanes algorithm 
