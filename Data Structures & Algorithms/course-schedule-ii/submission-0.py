class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        graph = {i: [] for i in range(numCourses)}

        # Build graph and indegree
        for i, j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
        
        q = deque([node for node in graph if indegree[node] == 0])
        order = []

        while q:
            node = q.popleft()
            order.append(node)

            for neighbours in graph[node]:
                indegree[neighbours]-=1
                if indegree[neighbours] == 0:
                    q.append(neighbours)
        
        if len(order) == numCourses:
            return order
        else:
            return []


        