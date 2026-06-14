class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, path, total):
            #Base Case
            if total == target:
                res.append(path[:])
                return
            if i >= len(nums) or total > target:
                return
            
            path.append(nums[i])
            backtrack(i+1, path, total+nums[i])
            path.pop()

            while(i+1 < len(nums) and nums[i] == nums[i+1]):
                i+=1
            backtrack(i+1, path, total)

        backtrack(0, [], 0)
        return res