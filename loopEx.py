# 출석번호가 1,2,3,4,5 앞에 100을 붙이기로 함 -> 101, 102, 103, 104, 105
students = [1,2,3,4,5]
print(students) # 1, 2, 3, 4, 5
students = [i+100 for i in students]
print(students) # 101, 102, 103, 104, 105

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "Groot"]
students = [len(i) for i in students]
print(students) # 8, 4, 5

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "Groot"]
students = [i.upper() for i in students]
print(students) # 'IRON MAN', 'THOR', 'GROOT'

'''
Quiz) 단신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
조건2 : 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2명
'''
from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51):  # 1~50 (승객 수)
    time = randrange(5, 51) # 5분~50분 소요시간
    if 5 <= time <= 15: # 매칭 성공 : 5분~15분 이내의 손님. 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:   # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0}명".format(cnt))