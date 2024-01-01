class Solution {
public:
    bool endsWithZero(int decimalNumber) {
    bitset<sizeof(int) * 8> binaryRepresentation(decimalNumber);

    return binaryRepresentation[0] == 0;
}
    bool hasTrailingZeros(vector<int>& nums) {
        int cnt = 0;
        for(int i=0;i<nums.size();i++){
            bool val = endsWithZero(nums[i]);
            if(val) {
                cnt ++;
            }
        }
        
        if(cnt >= 2) return true;
        return false;
    }
};
