class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = {}   #To store last occuring index of each ch
        for i in range(len(s)):
            hm[s[i]] = i
        
        res = []
        size = 0
        end = 0
        for i in range(len(s)):
            size+=1
            end = max(end, hm[s[i]])

            if i == end:
                res.append(size)
                size=0
        return res
