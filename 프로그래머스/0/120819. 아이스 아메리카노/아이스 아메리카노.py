def solution(money):
    coffee = 5500
    T1 = money // coffee
    T2 = money -(T1 *coffee)
    answer = [T1,T2]
    return answer