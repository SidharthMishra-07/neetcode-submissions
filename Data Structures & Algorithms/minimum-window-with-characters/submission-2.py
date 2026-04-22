class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        mp = {}
        hm = {}
        l=0
        count=0
        res = [-1, -1]
        reslen = float('inf')

        for ch in t:
            mp[ch] = mp.get(ch, 0)+1
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0)+1
            
            if s[r] in mp and hm[s[r]] == mp[s[r]]:
                count+=1

            while count == len(mp):
                if r-l+1 < reslen:
                    res = [l, r]
                    reslen = min(reslen, r-l+1)

                hm[s[l]]-=1
                if s[l] in mp and hm[s[l]] < mp[s[l]]:
                    count-=1
                l+=1
        l, r = res
        return s[l:r+1] if reslen!=float('inf') else ""

        