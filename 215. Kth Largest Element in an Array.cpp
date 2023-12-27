// used the sorting technique 
// if want to do without sorting use priority queue , you can use heap and quick sort technique 

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        return nums[nums.size()-k];
    }
};
