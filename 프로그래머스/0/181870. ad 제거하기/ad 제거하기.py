
'''
def solution(strArr):
    if 'ad' in strArr:
        strArr.remove('ad')
          
    return strArr
'''
def solution(strArr):
    return [s for s in strArr if 'ad' not in s]