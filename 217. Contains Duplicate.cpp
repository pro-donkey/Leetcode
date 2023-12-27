// Two approches 
// 1. First using Set data structure in stl T.C O(N) and S.C O(N)
// 2. Using sort function in the array T.C O(nlog n) 

// Approch 1
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> s;
        for(int i=0;i<nums.size();i++){
            if((s.find(nums[i]) != s.end())){
                return true;
            }
            else s.insert(nums[i]);
        }
        return false;
    }
};

// Approch 2
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        for(int i=1;i<nums.size();i++){
            if(nums[i-1] == nums[i]){
                return true;
            }
        }
        return false;
    }
};
