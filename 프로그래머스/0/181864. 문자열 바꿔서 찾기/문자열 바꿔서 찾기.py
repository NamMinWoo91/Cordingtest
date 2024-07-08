'''
def solution(myString, pat):
    A = list(myString)
    B = A.repalce('A', 'B')
    if B in pat:
        return 1
    else:
        return 0 '''

def solution(myString, pat):
    converted = myString.translate(str.maketrans('AB', 'BA'))
    return 1 if pat in converted else 0
    