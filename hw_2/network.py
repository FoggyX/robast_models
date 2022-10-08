import json
from collections import defaultdict
import heapq

def networkDelay(times, N: int, X: int):        
    net = defaultdict(list)
    
    for u, v, w in times:
        net[u].append((w, v))
    
    visited = set()

    heap = [(0, X)]

    while heap:
        time, node = heapq.heappop(heap)
        visited.add(node)
        
        if len(visited) == N:
            return time
        
        for cur_time, next_node in net[node]:
            if next_node not in visited:
                heapq.heappush(heap, (time + cur_time, next_node))
            
    return -1

if __name__ == "__main__":
    times_str = input("times: ")
    times = json.loads(times_str)
    N = int(input("N: "))
    X = int(input("X: "))
    print(networkDelay(times, N, X))
