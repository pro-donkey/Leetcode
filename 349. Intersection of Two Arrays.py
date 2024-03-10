class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st1 = set(nums1)
        st2 = set(nums2)
        ans = list(st1.intersection(st2))
        return ans




## Java Solution

import java.util.*;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        for (int num : nums1) {
            set1.add(num);
        }

        Set<Integer> set2 = new HashSet<>();
        for (int num : nums2) {
            set2.add(num);
        }

        set1.retainAll(set2);

        int[] ans = new int[set1.size()];
        int index = 0;
        for (int num : set1) {
            ans[index++] = num;
        }
        return ans;
    }
}
