import sys
import heapq

input = sys.stdin.readline


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 각 정점별 "상위 k개 짧은 거리"를 저장하는 최대힙(부호 반전으로 구현: -dist)
best = [[] for _ in range(n + 1)]

# 전역 우선순위큐(최소힙): (누적거리, 정점)
pq = []
heapq.heappush(pq, (0, 1))
heapq.heappush(best[1], 0)  # -0 == 0, 시작점까지 거리 0을 먼저 넣어 둠

while pq:
    cur_dist, u = heapq.heappop(pq)

    # u에서 나가는 간선 완화
    for v, w in graph[u]:
        nd = cur_dist + w

        if len(best[v]) < k:
            heapq.heappush(best[v], -nd)  # 최대힙처럼 쓰기 위해 -dist 저장
            heapq.heappush(pq, (nd, v))
        else:
            # 현재 v의 상위 k개 중 가장 큰 값(= k번째 후보 중 최댓값)보다 더 짧으면 교체
            largest = -best[v][0]
            if nd < largest:
                heapq.heapreplace(best[v], -nd)
                heapq.heappush(pq, (nd, v))

# 출력: 힙 크기가 k면 -best[i][0]이 k번째 최단거리, 아니면 -1
out = []
for i in range(1, n + 1):
    out.append(str(-best[i][0]) if len(best[i]) == k else "-1")
    
print("\n".join(out))

