def solution(my_string):
    answer = ''
    for i in my_string:
        answer += i.lower() if i.isupper() else i.upper()
    return answer