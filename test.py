
for r in range(int(input())):

    n, k = map(int, input().split())

    stroka = input()

    white = stroka[:k].count('W')
    res = white

    

    for i in range(n-k):
        
        if stroka[i] == 'W':
            white -= 1

        if stroka[i+k] == 'W':
            white += 1
        
        res = min(res, white)

    print(res)
    