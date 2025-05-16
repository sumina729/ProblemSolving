def solution(participant, completion):
    answer = ''
    
    hash_name = {}
    sum_hash = 0
    
    for name in participant:
        h = hash(name)
        hash_name[h] = name
        sum_hash+=h
    
    for name in completion:
        sum_hash -= hash(name)
    
    answer = hash_name[sum_hash]
    return answer