// using hashing and loop

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int ,int > mp;
        int ans = 0;
        for(auto &i: nums){
            ans += mp[i];
            mp[i]++;
        }
        return ans;
    }
};

// using  2 loops 


class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int ans = 0;
        for(int i=0;i<nums.size()-1;i++){
            for(int j=i+1;j<nums.size();j++){
                if(nums[i] == nums[j] && i<j){
                    ans +=1;
                }
            }
        }
        return ans;
    }
};
