def solution(num_list):
    answer = 0
    answer2 = 0
    for i in num_list:
        if i % 2 == 0 :
            answer += 1
            
        else :
            answer2 += 1
            
    return answer, answer2