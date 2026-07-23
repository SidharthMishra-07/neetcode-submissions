class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)

        for src, dest in tickets:
            adj[src].append(dest)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                res.append(v)
                adj[src].pop(i)
                if dfs(v) == True:
                    return True
                adj[src].insert(i, v)       #Backtrack
                res.pop()
            return False
        
        dfs("JFK")
        return res
