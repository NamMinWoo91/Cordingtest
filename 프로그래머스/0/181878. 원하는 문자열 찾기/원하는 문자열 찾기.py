def solution(myString, pat):
    AA = myString.upper()
    aa = pat.upper()
    
    if AA.find(aa) != -1:
        return 1
    else:
        return 0