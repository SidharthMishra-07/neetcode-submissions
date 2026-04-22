class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for char in t:
            if char not in freq:
                return False
            freq[char]-= 1
        for i in freq:
            if freq[i] != 0:
                return False
        return True
         
