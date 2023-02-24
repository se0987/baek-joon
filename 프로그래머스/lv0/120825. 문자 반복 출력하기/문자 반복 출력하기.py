def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n
    answer = ''.join(answer)
    return answer