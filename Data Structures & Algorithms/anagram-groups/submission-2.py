class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =[]
        hm = {}
        for s in strs:
            charArray = [0] * 26
            for ch in s:
                charArray[ord(ch) - ord('a')]+=1
            if tuple(charArray) in hm:
                hm[tuple(charArray)].append(s)
            else:
                hm[tuple(charArray)] = [s]
        
        for x in hm:
            res.append(hm[x])
        return res