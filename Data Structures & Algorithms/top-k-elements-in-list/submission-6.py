class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        arr = []
        for x, i in freq.items():
            arr.append([i, x])     #Changed values and key
        arr.sort(reverse=True)     #Sorts according to the first element of arr (here it is values)

        for i in range(k):
            res.append(arr[i][1])
        return res

        
        