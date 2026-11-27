class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        res = 10001
        currsum = 0

        for r in range(len(nums)):
            currsum += nums[r]

            while currsum >= target:
                res = min(res, r-l+1)
                currsum-= nums[l]
                l+=1
            
        return 0 if res == 10001 else res