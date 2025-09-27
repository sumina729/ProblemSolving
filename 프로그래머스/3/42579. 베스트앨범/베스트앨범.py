def solution(genres, plays):
    answer = []
    genres_num = {}
    genres_plays = {}
    max_genres = {}
    
    
    for i in range(len(genres)):
        if not genres[i] in genres_plays:
            genres_plays[genres[i]] = []
            max_genres[genres[i]] = 0
            
        genres_plays[genres[i]].append([i, plays[i]])
        max_genres[genres[i]] += plays[i]
        

    for g in genres_plays.keys():
        genres_plays[g].sort(key=lambda a : (-a[1], a[0]))
        
    print(max_genres)
    print(genres_plays)
    
    for _ in range(len(max_genres)):
        print(max_genres)
        max_key = max(max_genres, key=max_genres.get)
        print(max_key)
        max_genres[max_key] = 0
        
        if len(genres_plays[max_key]) == 1:
            answer.append(genres_plays[max_key][0][0])
        else:
            answer.append(genres_plays[max_key][0][0])
            answer.append(genres_plays[max_key][1][0])
    
    
    
        
    return answer