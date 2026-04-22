class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        res = 0
        for x in set1:
            if x-1 not in set1:
                curr = x
                count = 1
                while curr+1 in nums:
                    curr+=1
                    count+=1
                res = max(res, count)

        return res
