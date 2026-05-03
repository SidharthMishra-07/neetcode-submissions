class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            charArray = [0]*26
            for i in s:
                charArray[ord(i)-ord('a')] +=1
            if tuple(charArray) in hm:
                hm[tuple(charArray)].append(s) 
            else:
                hm[tuple(charArray)] = [s]
        ans = []
        for x in hm:
            ans.append(hm[x])
        return ans


