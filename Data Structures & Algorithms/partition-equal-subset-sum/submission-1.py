class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2 !=0:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)-1, -1, -1):
            temp = dp.copy()
            for t in dp:
                temp.add(t + nums[i])
            dp = temp
        return True if target in dp else False            