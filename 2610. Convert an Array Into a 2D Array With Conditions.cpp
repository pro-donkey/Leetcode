class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        vector<vector<int>>ans;
        unordered_map<int,int> mp;

        for(int i=0;i<nums.size();i++){
            mp[nums[i]]++;
        }

        while(!mp.empty()){
            vector<int> cnt ;
            for(auto it = mp.begin();it != mp.end();){
                cnt.push_back(it->first);
                it->second --;
                if(it->second == 0){
                    it = mp.erase(it);
                }
                else{
                    it ++;
                }
            }
            ans.push_back(cnt);
        }
        return ans;
    }
};
