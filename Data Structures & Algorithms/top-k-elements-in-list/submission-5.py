class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        arr = []
        for x, i in freq.items():
            arr.append([i, x])
        arr.sort(reverse=True)
        print(arr)
        for i in range(k):
            res.append(arr[i][1])
        return res

        
        