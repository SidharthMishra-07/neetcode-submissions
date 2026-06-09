class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            currsum = max(nums[i] + currsum, nums[i])
            res = max(currsum, res)
        return res