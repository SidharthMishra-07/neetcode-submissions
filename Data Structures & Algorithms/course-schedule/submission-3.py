class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        if len(prerequisites) == 0:
            return True

        for i, j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
        
        q = deque([node for node in graph if indegree[node] == 0])
        count = 0
        print(indegree)
        while q:
            node = q.popleft()
            count+=1
            for neighbours in graph[node]:
                indegree[neighbours]-=1
                if indegree[neighbours] == 0:
                    q.append(neighbours)
        print(graph)
        print(indegree)
        return count == numCourses