from cgi import test


test = ["A", "B", "C"]

test.append("D")
print(test)

test.remove("C")
print(test)

print(test.index("B")) # B의 위치 index

test.insert(1, "E") # index 1 위치에 삽입
print(test)

print(test.pop())
print(test)

num_list = [5,2,4,3,1,0]
num_list.sort() # 정렬
print(num_list)

num_list.reverse() # 역순 정렬
print(num_list)

#num_list.clear() # 모두 삭제
#print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["A", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)