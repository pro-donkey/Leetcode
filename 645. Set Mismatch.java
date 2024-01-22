class Solution {
    public int[] findErrorNums(int[] nums) {
        int [] arr = new int[2];
        int n = nums.length;
        int sum =0;
        HashSet<Integer> set = new HashSet<>();
        for(Integer it : nums){
            if(set.contains(it)){
                arr[0] = it;
            }
            else {
                set.add(it);
            }
            sum += it;
        }

        n = (n*(n+1))/2;
        arr[1] = n - sum + arr[0];

        return arr;
    }
}
