
        
        
def solution(phone_book):
    answer = True
    phone_book.sort()
    
    N = len(phone_book)
    for i in range(0, N-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True
    