class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, visit):
            #Base case:
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for i in range(len(nums)):
                if visit[i] == False:
                    visit[i] = True
                    perm.append(nums[i])

                    backtrack(perm, visit)

                    perm.pop()
                    visit[i] = False

        backtrack([], [False]*len(nums))
        return res