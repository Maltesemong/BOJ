score = int(input())

if score >= 90:
    GPA = 'A'

elif score >= 80:
    GPA = 'B'

elif score >= 70:
    GPA = 'C'

elif score >= 60:
    GPA = 'D'

else:
    GPA = 'F'

print(GPA)