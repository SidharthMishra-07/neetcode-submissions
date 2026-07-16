class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 
        graph = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for w in range(len(word)):
                pattern = word[:w] + "*" + word[w+1:]
                graph[pattern].append(word)

        visited = set()
        q = deque([beginWord])
        visited.add(beginWord)
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for w in range(len(word)):
                    pattern = word[:w] + "*" + word[w+1:]
                    for ch in graph[pattern]:
                        if ch not in visited:
                            visited.add(ch)
                            q.append(ch)
            res+=1

        return 0