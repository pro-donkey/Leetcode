class Solution {
    public int maxProduct(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        return ((nums[n-1] - 1)*(nums[n-2] -1));
    }
}



// cpp using priority queue
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        priority_queue<int> pq;
        for(int i=0;i<nums.size();i++){
            pq.push(nums[i]);
        }
        int num = 1;
        num *= (pq.top() -1);
        pq.pop();
        num *= (pq.top()-1);
        return num;
    }
};
