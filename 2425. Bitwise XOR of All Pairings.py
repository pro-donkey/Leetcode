class Solution:

    def calculate_xor(sefl, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums)):
            xor ^= nums[i]

        return xor

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        n, m = len(nums1), len(nums2)

        val1 = val2 = 0
        if n % 2:
            val1 ^= self.calculate_xor(nums2)
        if m % 2:
            val2 ^= self.calculate_xor(nums1)

        xor = val1 ^ val2

        return xor
