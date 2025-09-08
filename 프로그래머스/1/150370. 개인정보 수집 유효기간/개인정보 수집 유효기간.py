def get_day(day):
    a, b, c = map(int, day.split("."))
    return a*12*28 + b*28 + c

def solution(today, terms, privacies):
    answer = []
    
    today = get_day(today)
    
    terms_list = dict()
    
    for t in terms:
        t1, t2 = t.split()
        terms_list[t1] = int(t2)
    
        
    ans_list = []
    for i in range(len(privacies)):
        p = privacies[i]
        sday, b = p.split()
        
        sday = get_day(sday)
        sday += terms_list[b]*28
        
        # print(i+1, sday, today)
        if sday <= today:
            ans_list.append(i+1)
        
    
        
    return ans_list