import sys

'''
sys.stdin.readline() : 사용자 입력을 최대한 빠르게 받아야 하는 경우
rstrip() : 입력 후 자동으로 Enter 줄 바꿈 기호가 입력되므로 rstrip()을 함께 사용함
'''

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)


'''
input() : 한 줄의 문자열을 입력 받는 함수
map() : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용함
'''
# 예시) 공백을 기준으로 구분된 데이터를 입력받을 경우
list(map(int, input().split()))
# 예시) 공백을 기준으로 구분된 데이터의 갯수가 많지 않을 경우
a, b, c = map(int, input().split())


