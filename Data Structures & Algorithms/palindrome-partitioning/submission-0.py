class Solution:
    def isPal(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, part):
            #Base case
            if i == len(s):
                res.append(part[:])
                return
            
            for j in range(i, len(s)):
                if self.isPal(s, i, j):
                    part.append(s[i:j+1])
                    backtrack(j+1, part)
                    part.pop()
        
        backtrack(0, [])
        return res