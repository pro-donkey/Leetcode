class Solution {
    public int maxOperations(int[] nums, int k) {
        int cnt = 0;
        int left = 0;
        int right = nums.length - 1;
        Arrays.sort(nums);
        while(left < right){
            if(nums[left] + nums[right] == k){
                cnt += 1;
                left ++;
                right --;
            }
            else if(nums[left] + nums[right] > k){
                right --;
            }
            else {
                left ++;
            }
        }
        return cnt;
    }
}




/*
Your code implements a solution to find the maximum number of pairs in the array nums such that the sum of each pair equals k. Here's a breakdown of the steps:

Initialization:

Initialize the variable cnt to count the number of valid pairs.
Initialize the variables left and right to represent the pointers for the leftmost and rightmost elements of the sorted array, respectively.
Sort the input array nums in ascending order using Arrays.sort(nums).
Two Pointer Approach:

Use a two-pointer approach where left starts from index 0 and right starts from the last index of the array.
Iterate over the array while left is less than right.
Checking Sums:

If the sum of the elements at indices left and right equals k, increment the cnt variable to count this pair and move both pointers inward (left++ and right--).
If the sum is greater than k, decrement the right pointer to decrease the sum by moving it towards the left.
If the sum is less than k, increment the left pointer to increase the sum by moving it towards the right.
Termination and Return:

Return the total count of valid pairs (cnt) after the while loop terminates.
Overall, the code efficiently utilizes a two-pointer approach along with sorting to find the maximum number of pairs with a sum equal to k in the given array nums.

*/
