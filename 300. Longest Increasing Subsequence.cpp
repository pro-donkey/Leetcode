class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> arr;
        arr.push_back(nums[0]);
        int len = 1;

        for(int i=1;i<nums.size();i++){
            if(arr.back() < nums[i]){
                arr.push_back(nums[i]);
                len += 1;
            }
            else{
                int indx = lower_bound(arr.begin(),arr.end(),nums[i])-arr.begin();
                arr[indx] = nums[i];
            }
        }
        return len;
    }
};
