class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        l=0
        res = 0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1

            while hm[s[r]] > 1:
                hm[s[l]]-=1
                l+=1
            res = max(res, r-l+1)

        return res
