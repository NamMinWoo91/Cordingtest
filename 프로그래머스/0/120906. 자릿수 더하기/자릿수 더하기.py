def solution(n):
    answer = 0
    num_list = str(n)
    for i in num_list:      
        answer += int(i)
        
    return answer