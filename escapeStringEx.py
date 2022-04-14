# \n : 줄바꿈
print("백문이 불여일견 백견이 불여일타")
print("백문이 불여일견\n백견이 불여일타")

print('백문이 "불여일견" 백견이 불여일타') 
print("백문이 \"불여일견\" 백견이 불여일타")

# \\ : 문장 내에서 \ 로 바뀜
print("C:\\PythonWorkspace")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple ('Red ' 자리에 Pine을 덮어씀)

#\b : 백스페이스(한 글자 삭제)
print("Redd\bApple") # RedApple ('d' 삭제)

# \t : 탭
print("Red\tApple") # Red     Apple


# Quiz) 사이트 별로 비밀번호를 만들어주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 → naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 → naver
# 규칙3 : 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e'의 갯수 + '!'로 구성
#                        (nav)                      (5)                   (1)             (!)

# 예) 생성된 비밀번호 : nav51!

url = "http://youtube.com"
newPw = url.replace("http://", "") # 규칙 1
print(newPw)
newPw = newPw[:newPw.find(".")] # 규칙2
print(newPw)
strCnt = len(newPw) # 규칙 3 (글자 갯수)
eCnt = newPw.count("e") # 규칙 3 (글자 내 'e' 갯수)

print(newPw[:3] + str(strCnt) + str(eCnt) + "!")