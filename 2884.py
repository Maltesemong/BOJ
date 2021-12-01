a, b = map(int, input().split())
if b >= 45:
    print('{} {}'.format(a, b - 45))
elif a > 0 and b < 45:
    print('{} {}'.format(a-1, b + 15))
else:
    print('{} {}'.format(23, b + 15))
