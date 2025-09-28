import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while True:
    
    
        if scoville[0] >= K:
            break
            
        if len(scoville) == 1:
            return -1
            
        answer+=1
        
        n1 = heapq.heappop(scoville) 
        n2 = heapq.heappop(scoville)

        n3 = n1 + n2*2

        heapq.heappush(scoville, n3)
    
    return answer