class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, path):
            #Base case: Solution Complete
            if i == len(nums):
                res.append(path[:])
                return
            
            #Decision to include i
            path.append(nums[i])
            dfs(i+1, path)

            #Decision to exclude i
            path.pop()
            dfs(i+1, path)
        
        dfs(0, [])
        return res


            