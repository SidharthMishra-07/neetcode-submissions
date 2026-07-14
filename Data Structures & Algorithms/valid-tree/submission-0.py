class Solution:
    # A tree is an undirected graph with no cycles
    # A tree with n nodes must have exactly n - 1 edges — otherwise it’s invalid.
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(src, parent):
            visited.add(src)
            for nei in graph[src]:
                if nei not in visited:
                    dfs(nei, src)
                elif nei != parent:
                    return False    #cycle detected
            return True

        return dfs(0, -1) and len(visited) == n