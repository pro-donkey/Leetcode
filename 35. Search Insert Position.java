class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int size = nums.length;
        int right = size - 1;
        int x = 0;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid - 1;
                x = right + 1;
            } else {
                left = mid + 1;
                x = left;
            }
        }

        return x;
    }
}
