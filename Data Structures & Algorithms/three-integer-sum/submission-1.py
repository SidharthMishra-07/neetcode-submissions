class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums.sort()
        print(nums)

        for i in range(n-2):
            low = i+1
            high = n-1
            while low < high:
                target = -nums[i]
                if nums[low] + nums[high] == target:
                    res.add((nums[i], nums[low], nums[high]))
                    low+=1
                    high-=1
                elif nums[low] + nums[high] < target:
                    low+=1
                else:
                    high-=1
        return list(res)