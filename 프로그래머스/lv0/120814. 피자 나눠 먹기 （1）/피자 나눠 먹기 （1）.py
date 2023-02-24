def solution(n):
    answer = 0
    if not n%7:
        answer = n//7
    else: answer = n//7+1
    return answer