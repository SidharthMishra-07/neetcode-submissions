class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, path):
            #Base Case
            if i == len(nums):
                res.append(path[:])
                return
            
            # Include nums[i]
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()

            #Exclude
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1, path)

        backtrack(0, [])
        return res