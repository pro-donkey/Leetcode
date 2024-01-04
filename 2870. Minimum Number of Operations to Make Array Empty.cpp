class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_map<int,int> mp;
        for(int i=0;i<nums.size();i++){
            mp[nums[i]]++;
        }
        int cnt = 0;
        for(auto i : mp){
            if(i.second == 1) return -1;
            cnt += (i.second/3);
            if(i.second%3) cnt +=1;
        }
        return cnt;
    }
};
