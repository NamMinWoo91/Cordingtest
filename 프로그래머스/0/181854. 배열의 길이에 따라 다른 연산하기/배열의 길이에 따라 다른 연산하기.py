'''
def solution(arr, n):
   
    if len(arr) % 2 ==0: # arr 길이가 짝수 
        for digit in arr[0::1] # 모든 홀수 인덱스 위치
            digit += n 
    elif len(arr) % 2 !=0: # arr 길이가 홀수
        for digit in arr[0::2] # 모든 짝수 인덱스위치
            digit += n
        
    return arr
    '''
def solution(arr, n):
    if len(arr) % 2 == 0:  # arr 길이가 짝수
        for i in range(1, len(arr), 2):  # 모든 홀수 인덱스 위치
            arr[i] += n
    else:  # arr 길이가 홀수
        for i in range(0, len(arr), 2):  # 모든 짝수 인덱스 위치
            arr[i] += n
    
    return arr