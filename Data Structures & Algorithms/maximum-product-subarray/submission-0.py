class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1, 1
        for num in nums:
            temp = currMax * num
            currMax = max(num, num*currMax, num*currMin)
            currMin = min(num, temp, num*currMin)
            res = max(res, currMax)
        
        return res