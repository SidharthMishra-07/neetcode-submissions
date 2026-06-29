class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Building the graph
        graph = defaultdict(list)
        for i in range(len(times)):
            src = times[i][0]
            dest = times[i][1]
            weight = times[i][2]
            graph[src].append((dest, weight))

        time = [float("inf")] * (n+1)
        time[k] = 0

        # Min-heap
        pq = []
        heapq.heappush(pq, (0, k)) #(time, node)

        count = 0
        while pq:
            curr_time, node = heapq.heappop(pq)

            if curr_time > time[node]:
                continue

            for neighbour, weight in graph[node]:
                if time[node] + weight < time[neighbour]:
                    time[neighbour] = time[node] + weight
                    heapq.heappush(pq, (weight, neighbour))
        
        max_time = max(time[1:])
        return max_time if max_time != float("inf") else -1
