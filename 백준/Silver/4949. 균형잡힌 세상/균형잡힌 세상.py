while True:
    txt = input()
    stack = []
    if txt == '.':
        break

    try:
        for t in txt:

            if not t in ['(', ')', '[', ']']:
                continue

            if t == '(':
                stack.append(t)
            elif t == '[':
                stack.append(t)
            elif t == ')':
                a = stack.pop()
                if a != '(':
                    print('no')
                    break
            elif t == ']':
                a = stack.pop()
                if a != '[':
                    print('no')
                    break
        else:
            if stack != []:
                print('no')
            else: print('yes')
    except:
        print('no')