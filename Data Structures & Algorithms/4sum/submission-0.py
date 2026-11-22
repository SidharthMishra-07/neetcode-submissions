class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()

        for i in range(n-3):
            for j in range(i+1, n-2):
                low = j+1
                high = n-1
                while low < high:
                    curr_sum = (nums[i] + nums[j] + nums[low] + nums[high])
                    if curr_sum == target:
                        res.add((nums[i], nums[j], nums[low], nums[high]))
                        low+=1
                        high-=1
                    elif curr_sum < target:
                        low+=1
                    else:
                        high-=1
        return list(res)
