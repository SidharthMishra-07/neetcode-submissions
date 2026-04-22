class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        mp = {}
        hm = {}
        l=0
        for ch in s1:
            mp[ch] = mp.get(ch, 0) + 1

        for r in range(len(s2)):
            hm[s2[r]] = hm.get(s2[r], 0) + 1

            #Slide Window if size exceeds 3
            while r-l+1 > len(s1):
                hm[s2[l]]-=1
                if hm[s2[l]]==0:
                    del hm[s2[l]]
                l+=1
                        
            if hm==mp:
                return True
        return False

                
            

            
            