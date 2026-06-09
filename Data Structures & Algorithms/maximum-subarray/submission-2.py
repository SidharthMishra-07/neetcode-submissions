class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currsum = 0
        for num in nums:
            if currsum < 0:
                currsum = 0
            currsum+= num
            maxSub = max(maxSub, currsum)
        return maxSub