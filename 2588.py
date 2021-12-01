a = list(map(int, input()))
b = list(map(int, input()))


result_1 = (100 * a[0] + 10 * a[1] + a[2]) * b[2]
result_2 = (100 * a[0] + 10 * a[1] + a[2]) * b[1]
result_3 = (100 * a[0] + 10 * a[1] + a[2]) * b[0]

result = result_3 * 100 + result_2 * 10 + result_1

print(result_1)
print(result_2)
print(result_3)
print(result)
