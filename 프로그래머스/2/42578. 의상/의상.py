from itertools import combinations

def solution(clothes):
    answer = 1
    
    kind_cnt = {}
    
    for c, k in clothes:
        if not k in kind_cnt:    
            kind_cnt[k] = 0
        kind_cnt[k] +=1
    
    print(kind_cnt)
    
    
    for cnt in kind_cnt.values():
        answer*= cnt+1 # 입지 않는 경우 추가
        
    
    return answer-1