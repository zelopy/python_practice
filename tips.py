'''
일반적인 알고리즘 문제 해결 과정
1. 지문 읽기 및 컴퓨터적 사고
2. 요구사항(복잡도) 분석
3. 문제 해결을 위한 아이디어 찾기
4. 소스코드 설계 및 코딩
'''


# 수행 시간 측정 방법
import time

start_time = time.time() # 측정 시작
end_time = time.time() # 측정 종료
print("time: ", end_time - start_time) # 수행 시간 출력


'''
실전에서 유용한 표준 라이브러리
 itertools : 
 - 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공
 - 특히 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용됨
 heapq : 
 - 힙(Heap) 자료구조 제공
 - 일반적으로 우선순위 큐 기능을 구현하기 위해 사용
 bisect :
 - 이진 탐색(Binary Search) 기능을 제공
 collections : 
 - 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함
 math : 
 - 필수적인 수학적 기능 제공
 - 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함
'''


# 자주 사용되는 내장 함수
# sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

# eval()
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array = [('AAA', 50), ('BBB', 32), ('CCC', 74)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)