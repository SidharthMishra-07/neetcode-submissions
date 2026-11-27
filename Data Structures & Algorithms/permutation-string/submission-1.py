class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm1 = {}
        hm2 = {}
        l=0

        for i in range(len(s1)):
            hm1[s1[i]] = hm1.get(s1[i], 0) + 1
        
        for r in range(len(s2)):
            hm2[s2[r]] = hm2.get(s2[r], 0) + 1

            while r-l+1 > len(s1):
                hm2[s2[l]]-=1
                if hm2[s2[l]] == 0:
                    del hm2[s2[l]]
                l+=1

            if hm1 == hm2:
                return True

        return False    
        