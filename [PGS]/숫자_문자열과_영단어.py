def solution(s):
    change=['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for i,value in enumerate(change):
        s=s.replace(value,str(i))
    answer=int(s)
    return answer