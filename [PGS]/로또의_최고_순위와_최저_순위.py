def solution(lottos, win_nums):
    answer = []
    a=0
    for i in lottos:
        if i in win_nums:
            a+=1
            
    answer.append(lottos.count(0)+a)
    answer.append(a)
    
    
    rank=[6,6,5,4,3,2,1]
    
    answer=[rank[i] for i in answer]
    return answer