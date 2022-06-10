'''
람다 표현식
특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있음
 - 함수 자체가 간단한 경우
 - 어떠한 함수 자체를 입력받는 함수를 사용하는 경우
'''

# 일반적인 add() 메서드 사용
def add(a, b):
	return a + b
print(add(3, 7))


# 람다 표현식으로 구현한 add() 메서드
print( (lambda, a, b: a + b)(3, 7) )


'''
Quiz) 아래 리스트를 점수 순으로 오름차순 정렬
'''
array = [('AAA', 50), ('BBB', 32), ('CCC', 74)]

# 일반적인 방법
def my_key(x):
	return x[1] # 두 번째 원소 반환

print(sorted(array, key=my_key)) # 반환된 두 번째 원소(점수)를 정렬의 기준으로

# lambda 표현식을 이용한 방법
print(sorted(array, key=lambda x: x[1]))
