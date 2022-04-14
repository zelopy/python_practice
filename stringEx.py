python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # n번째 글자가 대문자인지
print(len(python)) # 문자열 길이
print(python.replace("Python", "Java"))

index = python.index("n") # 첫번째로 나오는 'n'의 위치
print(index)
index = python.index("n", index + 1) # 첫번째 'n' 이후의 위치부터 그 다음 'n' 위치 찾기
print(index)

print(python.find("Java")) # 찾는 글자가 없을 경우 : -1 반환
print(python.index("Java")) # 찾는 글자가 없을 경우 : 오류 발생

print(python.count("n")) # 'n'이 총 몇 번 나오는지
