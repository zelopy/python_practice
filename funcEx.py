def open_account():
    print("새로운 계좌 생성 완료")

open_account()  # 함수 호출

# 입금
def deposit(balance, money):
    print("입금 완료 (잔액: {0}원)".format(balance + money))
    return balance + money

# 출금
def withdraw(balance, money):
    if balance >= money:
        print("출금 완료 (잔액: {0}원)".format(balance - money))
        return balance - money
    else:
        print("출금 실패 (잔액: {0}원)".format(balance))
        return balance

# 저녁에 출금(수수료 추가)
def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance,2000)
print(balance)

commission, balance = withdraw_night(balance, 500)
print("수수료:{0}원, 잔액은 {1}원".format(commission, balance))


# 함수 기본값 설정
def profile(name, age=17, main_lang="Python"):
    print("이름:{0}, \t나이:{1}, \t사용언어:{2}".format(name, age, main_lang))

profile("ABC")  # 이름:ABC,       나이:17,        사용언어:Python


# 함수 키워드를 사용한 호출 방법
def profile_keyword(name, age, main_lang):
    print(name, age, main_lang)

profile_keyword(age=30, main_lang="JAVA", name="ABC")


# 가변 인자
def profile_dynamic(name, age, *lang):
    print("이름:{0}, \t나이:{1}, \t".format(name, age), end=" ")
    for lang in lang:
        print(lang, end=" ")
    print()

profile_dynamic("A", 20, "JAVA", "Python", "C", "C++", "C#")
profile_dynamic("B", 33, "Kotlin", "Swift")