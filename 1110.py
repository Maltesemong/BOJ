N = int(input())
temp = N
i = 1
while True:
    if N < 10:
        a = 0
        b = N
    else:
        a = N // 10
        b = N - (10 * a)
    if a + b >= 10:
        c = a + b - 10
    else:
        c = a + b
    new_num = 10 * b + c
    if new_num == temp:
        print(i)
        break
    else:
        i += 1
        N = new_num



        
        
