class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        for i in freq:
            if freq[i] > 1:
                return i
        return -1