print("Python", "Java") # Python Java
print("Python", "Java", sep=" vs ")   # Python vs Java
print("Python", "Java", sep=", ", end="?")  # Python, Java?

print("\n===============================")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# ljust, rjust
scores = {"수학":0, "영어":50, "코딩":100}  # Dictionary
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")  # n칸 만큼 공간을 확보한 후 왼쪽 or 오른쪽 정렬
#수학      :   0
#영어      :  50
#코딩      : 100

# zfill
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))    # n 공간만큼 확보하고, 빈 공간은 0으로 채움

# 키 입력(사용자 키 입력은 무조건 문자열 형태로 자동 변환됨)
answer = input("입력하세요 : ")
print("입력 값 : " + answer)