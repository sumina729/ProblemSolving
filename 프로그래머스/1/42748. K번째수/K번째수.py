def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        new_array = array[i-1:j]
        new_array.sort()
        answer.append(new_array[k-1])
        # print(new_array)
    return answer