class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        res = []

        def dfs(graph, node, component):
            if node not in visited:
                visited.add(node)
                component.append(node)

                for neighbour in graph[node]:
                    dfs(graph, neighbour, component)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        for node in graph:
            if node not in visited:
                component = []
                dfs(graph, node, component)
                res.append(component)

        if n-len(graph)!=0:
            return len(res) + n-len(graph)
        else:
            return len(res)
