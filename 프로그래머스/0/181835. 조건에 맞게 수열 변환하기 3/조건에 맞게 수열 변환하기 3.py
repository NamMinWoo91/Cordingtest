def solution(arr, k):
    answer = []
    if k % 2 == 0:  # k가 짝수일 때
        for i in arr:
            answer.append(i + k)
    else:  # k가 홀수일 때
        for i in arr:
            answer.append(i * k)
    return answer
  