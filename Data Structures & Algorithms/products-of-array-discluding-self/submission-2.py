class Solution:
    #Brute force O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        pro0 = 1
        zeroCnt=0

        for i in nums:
            if i ==0:
                zeroCnt +=1
            pro = pro * i   

        if zeroCnt > 1:
            return [0]*len(nums)

        for i in nums:
            if i ==0:
                continue
            pro0 = pro0*i
        
        res=[]
        for i in nums:
            if i == 0:
                res.append(pro0)
                continue
            res.append(pro//i)
        return res