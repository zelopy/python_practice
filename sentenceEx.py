sentence = 'AAA'
print(sentence)

sentence2 = "BBB"
print(sentence2)

sentence3 = """
CCC
DDD
EEE
"""
print(sentence3) # 위, 아래 공백 라인 추가되어 5줄

jumin = "800102-1234567"

print("성별 : " + jumin[7]) # 1
print("연도 : " + jumin[0:2]) # 0부터 2 직전까지 : 0,1 자리값만
print("월 : " + jumin[2:4])  # 2부터 4 직전까지 : 2,3 자리값만
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지(시작이 0번째인 경우엔 생략 가능)
print("뒤 7자리 : " + jumin[7:]) # 끝까지인 경우엔 마지막 생략 가능
print("뒤 7자리(뒤에서부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지
