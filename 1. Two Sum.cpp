class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i=0;i<nums.size()-1;i++){
            for(int j=i+1;j<nums.size();j++){
                if(nums[i]+nums[j] == target){
                    return {i,j};
                }
            }
        }
        return {-1,-1};
    }
};



// using unordered_map
// O(n) - time
// O(n) - space




class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mp;
        for(int i=0;i<nums.size();i++){
            int val = target - nums[i];
            if(mp.find(val) != mp.end()){
                return {mp[val], i};
            }
            else {
                mp[nums[i]] = i;
            }

            
        }
        return {-1,-1};
    }
};
