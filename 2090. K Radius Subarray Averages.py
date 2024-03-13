class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        n = len(nums)
        res = [-1] * n
        win_size = 2 * k + 1
        left = 0
        pref_sums = []
        pref_sum = 0
        for num in nums:
            pref_sum += num
            pref_sums.append(pref_sum)
        for right in range(n):
            if right - left + 1 == win_size:
                if left > 0:
                    win_sum = pref_sums[right] - pref_sums[left - 1]
                else:
                    win_sum = pref_sums[right]
                avg = win_sum // win_size
                res[k] = avg
                k += 1
                left += 1
        return res
