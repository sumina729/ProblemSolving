def solution(id_list, report, k):
    reports = set(report) # 중복제거
    
    b_call_n = dict() #b의 신고수
    a_call_id = dict() #a가 신소한 b
    a_call_n = dict() #a가 신고 한거 중에 정지된 유저의 수
    for id in id_list:
        b_call_n[id] = 0
        a_call_n[id] = 0
        a_call_id[id] = set()
    
    
    for r in reports: #신고체크
        a, b = r.split()
        # print(a, b)
        
        b_call_n[b]+=1
        a_call_id[a].add(b)

    
    for id_b in id_list:
        if b_call_n[id_b] >= k: #k 이상이면 
            
            for id_a in id_list:
                if id_b in a_call_id[id_a]:
                    a_call_n[id_a] +=1
    
    answer = []
    for id in id_list:
        answer.append(a_call_n[id])
    
    return answer