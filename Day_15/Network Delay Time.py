from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list (directed graph)
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))

        # Distance array
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        # Min-heap: (distance, node)
        heap = [(0, k)]

        while heap:
            d, u = heappop(heap)

            # Ignore outdated entries
            if d > dist[u]:
                continue

            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heappush(heap, (dist[v], v))

        # Get maximum distance (ignore index 0)
        ans = max(dist[1:])

        return -1 if ans == float("inf") else ans
