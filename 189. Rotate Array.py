class Solution:
    def reverse(self, nums:List[int],start : int , end : int) -> None:
        while start <= end :
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        self.reverse(nums,0,n-k-1)
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-1)
        
