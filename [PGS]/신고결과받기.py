def solution(id_list, report, k):
    answer = []
    
    #중복 신고 제거
    report=list(set(report))
    
    #피신고 계정 리스트화
    reported=[]
    for i in report:
        reported.append(i.split()[1])
    
    #정지계정 리스트화
    suspen=[]
    for i in id_list:
        if reported.count(i)>=k:
            suspen.append(i)
    
    #신고후 정지처리 메일개수 딕셔너리화
    m_n={}
    for i in id_list:
        m_n[i]=0

    for i in report:
        if i.split()[1] in suspen:
            m_n[i.split()[0]]+=1
    #정답 리스트화
    for i in id_list:
        answer.append(m_n[i])   

    return answer



# 숏코드
def solution(id_list, report, k):
    
    report=set(report)
    re_n={i:0 for i in id_list}
    
    for i in report:
        re_n[i.split()[1]]+=1
    m_l=[i.split()[0] for i in report if re_n[i.split()[1]] >=k]
    answer=[m_l.count(i) for i in id_list]
    return answer