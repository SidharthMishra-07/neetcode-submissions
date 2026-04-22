class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            curr = nums[i]
            count = 1
            while curr+1 in nums:
                curr+=1
                count+=1
            res = max(res, count)

        return res
