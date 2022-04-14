print("a" + "b") # ab
print("a", "b") # a b

# 방법 1
print("나는 %d살입니다." % 99) # %d는 정수값
print("나는 %s을 좋아합니다." % "파이썬") # %s는 문자열
print("Apple 은 %c로 시작해요." % "A") # %c는 1개 글자(character)

# Tip : %s로 모두 사용 가능

print("나는 %s색과 %s색을 좋아합니다." % ("파랑", "빨강"))

# 방법 2
print("나는 {}살 입니다.".format(99))
print("나는 {}색과 {}색을 좋아합니다.".format("파랑", "빨강"))
print("나는 {0}색과 {1}색을 좋아합니다.".format("파랑", "빨강"))
print("나는 {1}색과 {0}색을 좋아합니다.".format("파랑", "빨강"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 99, color = "파랑"))

# 방법 4 (v3.6 이상)
age = 77
color = "노랑"
print(f"나는 {age}살이며, {color}색을 좋아합니다.")