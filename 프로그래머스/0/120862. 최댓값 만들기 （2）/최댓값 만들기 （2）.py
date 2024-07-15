def solution(numbers):
    numbers2 = sorted(numbers)
    mini =numbers2[0] * numbers2[1]
    maxi = numbers2[-1] * numbers2 [-2]
    answer = max(mini,maxi)
    return answer