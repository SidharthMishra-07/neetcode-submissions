class Solution:
    def reverse(self, nums, l, r):
        low = l
        high = r
        while(low < high):
            nums[low], nums[high] = nums[high], nums[low]
            low+=1
            high-=1


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)