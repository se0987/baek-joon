years = int(input())

if years % 4 == 0:
    if years % 400 == 0:
        result = 1
    elif years % 100 == 0:
        result = 0
    else:
        result = 1
else: result = 0

print(result)