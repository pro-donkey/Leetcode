class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                sm = nums[i] + nums[j] + nums[k]
                if sm > 0:
                    k -= 1
                elif sm < 0:
                    j += 1
                else:
                    arr = [0] * 3
                    arr[0], arr[1], arr[2] = nums[i], nums[j], nums[k]
                    ans.append(arr)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans
