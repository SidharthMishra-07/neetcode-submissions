class Solution:
    #Bucket Sort Solution
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = [[] for _ in range(len(nums)+1)]
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        
        for num, cnt in freq.items():
            res[cnt].append(num)

        ans = []
        for i in range(len(res)-1, 0, -1):
            for x in res[i]:
                ans.append(x)
                if len(ans) == k:
                    return ans 

        
        
        
        