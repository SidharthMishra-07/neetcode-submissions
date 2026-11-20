class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = 0, 0
        n1, n2 = len(word1), len(word2)
        res = ""

        while l1<n1 and l2<n2:
            res+=word1[l1]
            l1+=1
            res+=word2[l2]
            l2+=1
        while l1<n1 and l2>=n2:
            res+=word1[l1]
            l1+=1
        while l2<n2 and l1>=n1:
            res+=word2[l2]
            l2+=1
        return res