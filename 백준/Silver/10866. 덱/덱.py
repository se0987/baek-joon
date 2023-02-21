def dequ(command):
    if 'push' in command:
        command, x = map(str, command.split())
        x = int(x)
        if 'front' in command:
            dq.insert(0, x)
        elif 'back' in command:
            dq.append(x)
    elif 'pop' in command:
        if len(dq) == 0:
            print(-1)
        else:
            if 'front' in command:
                print(dq.pop(0))
            elif 'back' in command:
                print(dq.pop())
    elif 'size' in command:
        print(len(dq))
    elif 'empty' in command:
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in command:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif 'back' in command:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])

import sys

N = int(sys.stdin.readline())
dq = []
for n in range(N):
    command = sys.stdin.readline()
    dequ(command)

