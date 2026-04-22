class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        res = []
        for i,x in enumerate(nums):
            if (target - x) in hm:
                res.append(hm.get(target - x)) 
                res.append(i)  
            hm[x] = i
        return res        