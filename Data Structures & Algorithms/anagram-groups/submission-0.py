class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] +=1
            key = tuple(count)  # immutable, hashable key
            freq[key].append(s)
        return list(freq.values())



#ProTip: Use defaultdict() when u want to get the output as 'List[List[str]]'