import sys

l_string = list(sys.stdin.readline().strip())
r_string = []

for _ in range(int(sys.stdin.readline())):

    command = sys.stdin.readline().strip()  # 계행문자 제거
    # L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시)
    # l_string -> r_string(역순)
    if command[0] == 'L':
        if l_string:
            r_string.append(l_string.pop())
    # D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시)
    # r_string -> l_string
    elif command[0] == 'D':
        if r_string:
            l_string.append(r_string.pop())
    # B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시)
    elif command[0] == 'B':
        if l_string:
            l_string.pop()
    # P $	$라는 문자를 커서 왼쪽에 추가함
    else:
        command, x = map(str, command.split())
        l_string.append(x)


l_string.extend(reversed(r_string))
print(''.join(l_string))
