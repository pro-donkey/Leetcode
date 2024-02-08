class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int mx = Integer.MIN_VALUE;
        while(left <= right){
            int area = Math.min(height[left],height[right]);
            area = area*Math.abs(left-right);
            mx = Math.max(mx,area);
            if(height[left] > height[right]){
                right --;
            }
            else if(height[left] == height[right]){
                left ++;
                right --;
            }
            else {
                left ++;
            }
        }

        return mx;
    }
}

// here is the explaination of the code 
/*
1. The maxArea method takes an integer array height as input, representing the heights of the lines.

2. It initializes two pointers, left and right, at the beginning and end of the array respectively.

3.  It also initializes a variable mx (short for maximum) to Integer.MIN_VALUE, which will be used to track the maximum area found so far.

4.  The method enters a while loop that continues as long as the left pointer is less than or equal to the right pointer.

5.  Inside the loop, it calculates the current area formed by the lines at the positions indicated by the left and right pointers. This is done by taking the minimum height between the lines (to represent the height of the water) and multiplying it by the distance between the lines (which is the absolute difference between the left and right pointers).

6.  It updates the mx variable with the maximum of its current value and the calculated area.
*/

