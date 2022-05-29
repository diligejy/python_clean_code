# for - else는 절대 사용하지 말 것

for i in range(3):
    print("Loop", i)
else:
    print("Else block!")

for i in range(3):
    print("Loop", i)
    if i == 1:
        break
else:
    print("Else block!")

for x in []:
    print("이 줄은 실행되지 않음")
else:
    print("For Else Block!")
