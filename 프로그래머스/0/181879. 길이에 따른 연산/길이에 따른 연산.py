def solution(num_list):
    answer = 0
    answer1 = 1
    if len(num_list) >= 11:
        for i in num_list:
            answer += i
        return answer
    else:
        for i in num_list:
            answer1 *= i
        return answer1
            
