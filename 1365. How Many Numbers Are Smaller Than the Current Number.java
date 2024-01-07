class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int n = nums.length;
        int [] arr = new int [n];
        HashMap<Integer,Integer> mp = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int cnt = 0;
             for(int j=0;j<n;j++){
                 if(i == j) continue;
                 if(nums[j] < nums[i]){
                     cnt += 1;
                 }
             }
             mp.put(nums[i],cnt);
        }

        for(int i=0;i<n;i++){
            arr[i] = mp.get(nums[i]);
        }
        return arr;
    }
}
