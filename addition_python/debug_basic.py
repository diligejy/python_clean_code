def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = 175
gender = "남성"
weight = std_weight(height / 100, gender)
weight = round(weight, 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다".format(height, gender, weight))
