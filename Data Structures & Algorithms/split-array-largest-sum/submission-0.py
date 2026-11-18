class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        res = high
        while low <= high:
            mid = (low+high) // 2
            cap = mid
            count = 1
            for num in nums:
                if cap - num < 0:
                    count+=1
                    cap = mid
                cap -= num

            if count <= k:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res
                