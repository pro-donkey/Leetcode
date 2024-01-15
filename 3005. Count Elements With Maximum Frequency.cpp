class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int, int> map;

        for(int i=0;i<nums.size();i++){
            map[nums[i]]++;
        }
        int mx = -1;
        
        for(auto it : map){
            if(it.second >= mx){
                mx = it.second;
            }
        }

        int cnt = 0;
        for(auto it: map){
            if(it.second == mx){
                cnt += it.second;
            }
        }


        return cnt;
    }
};
