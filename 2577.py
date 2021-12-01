A = int(input())
B = int(input())
C = int(input())
D = list(str(A * B * C))
E = list(map(int, D))

for i in range(10):
    print('{}'.format(E.count(i)))