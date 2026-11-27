class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        l=0
        res = 0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0)+1

            maxFreq = max(hm.values())

            while r-l+1 - maxFreq > k:
                hm[s[l]]-=1
                l+=1

            res = max(res, r-l+1)
        return res 