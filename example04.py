# 51 구구단
# 19단 출력
import sys
print('''
            Multiplication Table
        1    2    3    4    5    6   7     8    9 
    -----------------------------------------------
1  |    1    2    3    4    5    6    7    8    9
2  |    2   4   
3  |    3   6
4  |    4   8
5  |    5   10
6  |    6   12
7  |    7   14
8  |    8   16
9  |    0   18
''')

print('''
            Multiplication Table
        1    2    3    4    5    6   7     8    9 
    -----------------------------------------------
''', end='')
for i in range(1, 9+1):
    print(f'{i}|  1    2   3   4   5   6   7   8   9')



print('''
            Multiplication Table
        1    2    3    4    5    6   7     8    9 
-------------------------------------------------------
''', end='')
for i in range(1, 9+1):   # 헤더부분
    print(f'{i}  |',end='')     #왼쪽세로부분
    for j in range(1, 9+1):
        print(f'{i * j:4d}', end='')
    print()


# 33
cardno = input('카드번호는? ')

result = '잘못된 카드 번호입니다'
if cardno[:2] == '35':                 #cardno이 33으 시작하면?
    if cardno == "356317": result = 'JCB카드 NH농협카드'
    elif cardno == "356901": result = 'JCB카드 신한카드'
    elif cardno == "356912": result = '비자카드 신한카드'
elif cardno[:1] == '4':                       #cardno이 4로 시작하면?
    if cardno == "404825": result = '비자카드 KB국민카드'
    elif cardno == "438676": result = '마스터카드 신한카드'
elif cardno[:1] == '5':                       #cardno이 5로 시작하면?
    if cardno == "524353": result = '마스터카드 외환카드'
    elif cardno == "540926": result = '마스터카드 KB국민카드'

print(f'{cardno} / {result}')

# if cardno == 356317: result = 'JCB카드 NH농협카드'
# elif cardno == 356901: result = 'JCB카드 신한카드'
# elif cardno == 356912: result = '비자카드 신한카드'
# elif cardno == 404825: result = '비자카드 KB국민카드'
# elif cardno == 438676: result = '마스터카드 신한카드'
# elif cardno == 524353: result = '마스터카드 외환카드'
# elif cardno == 540926: result = '마스터카드 KB국민카드'
#
# print(f'{cardno} / {result}')


# 16 개선하기 - 리스트/반복문/함수

price = 34_560
paid = 50_000
charge = paid - price

charges = []
moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for money in moneys:
    charges.append(charge // money)
    charge %= 10000

result = f'''
금액 : {price:,}원
지불금액 : {paid:,}원
잔돈 : {(paid - price):,} 원
------------
'''
for idx, m in enumerate(moneys):
    result += f'{m}원 : {charges[idx]} 장/개\n'

print(result)

def compute_charge(price, paid):
    pass

# 16 개선하기 - 리스트/반복문/함수

price = 34_560
paid = 50_000
charge = paid - price

charges = []
moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for money in moneys:
    charges.append(charge // money)
    charge %= 10000

result = f'''
금액 : {price:,}원
지불금액 : {paid:,}원
잔돈 : {(paid - price):,} 원
------------
'''
for idx, m in enumerate(moneys):
    result += f'{m}원 : {charges[idx]} 장/개\n'

print(result)

#####################

def compute_charge(price, paid):
    charges = []
    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    charge = paid - price
    for money in moneys:
        charges.append(charge // money)
        charge %= 10000

    result = f'''
    금액 : {price:,}원
    지불금액 : {paid:,}원
    잔돈 : {(paid - price):,} 원
    ------------
    '''
    for idx, m in enumerate(moneys):
        result += f'{m}원 : {charges[idx]} 장/개\n'

    print(result)

# 잔돈 구하는 함수 호출 및 테스트
price = int(input('지불해야 할 금액은? '))
paid = int(input('받은 금액은? '))
compute_charge(price, paid)

# 변수의 유효범위scope
# scope: 변수가 접근 가능한 범위를 의미
# 전역 scope: 프로그램의 최상위 레벨에서 정의된 변수
#            어느 곳에서나 접근 가능
#            함수내에서 전역변수에 접근(사용) 가능
#            단, 전역변수를 함수내에서 수정시 global 이라는 키워드 필요!

# 지역 scope:  반복문 내부 / 함수 내부에 정의된 변수
#             반복문이나 함수 내에서만 접근 가능
#             반복문 실행 종료나 함수 호출이 끝나면 자연 소멸

x = 10  # 전역변수
y = 10

def func():
    x = 20
    print('func : x = ', x)

def func2():
    global y    # 함수내에서 전역변수를 제어하기 위해 global 선언
    y = 20
    print('func : x = ', y)

print(x)    # x 출력
func()      # x 변수가 있는 함수 호출
print(x)

print(y)
func2()
print(y)

# 웹 사이트 방문 누적 횟수 누적 프로그램
visits = 0

isflag = False
while isflag:
    menu = input('1. 웹사이트 방문 2. 종료 : ')
    if menu == '1':
        visits += 1
        print('누적 방문 횟수 : ', visits)
    else:
        print('방문을 종료합니다!')
        isflag = False

# 누적 방문자 수 처리 함수 정의
def count_visitor():
    global visits
    visits += 1
    print('누적 방문 횟수 : ', visits)


isflag = True
while isflag:
    menu = input('1. 웹사이트 방문 2. 종료 : ')
    if menu == '1':
        count_visitor()
        print('누적 방문 횟수 : ', visits)
    else:
        print('방문을 종료합니다!')
        isflag = False

# ----------------------
goods = 1
goodsCount = [5, 2, 10, 3]


def printReceipt():
    total = 0
    total = 1000 * goodsCount[0] # 리스트는 참조(주소) 자료형이므로
                                 # 별다른 코드 없이 해당 변수 접근가능
    print('total : ', total)

    goodsCount[0] = 10           # 함수내에서 global없이 리스트의 일부 변경가능
    total2 = 1000 * goodsCount[0]
    print('total2 : ', total2)

    # goodsCount = [99,99,99,99]    # 전역변수 자체를 변경하려고 시도시
                                    # 오류발생! - global 필요!!

    print('goodsCount[0] : ', goodsCount[0])
    goodsCount[0] = 10
    # print(goods)    #goods 라는 변수가 선언 안되어 있음
                    # goods 라는 변수가 없는데 호출해서 출력 시도 - 실패
    goods = 5       # goods 변수 선언후 5라는 값 저장 - 성공

printReceipt()
print(goodsCount[0])
print(goods)

# 26 - 세금 계산 computeTax
def computeTax():
    tax = 0
    if isMarried == 0:
        tax = salary * 0.1
        if salary >= 3000:
            tax = salary * 0.25
    elif isMarried == 1:
        tax = salary * 0.15
        if salary >= 6000:
            tax = salary * 0.35

     print(f'''
     결혼여부 : {isMarried}, 연봉 : {salary:,}
     세금 : {tax:,}''')

# 데이터 입력 및 함수 호출
isMarried = int(input('결혼여부는? 0:미혼, 1:기혼 '))
salary = int(input('연봉은? '))

computeTax(isMarried, salary)

# 27 - 윤년 구분 isLeapYear
def isLeapYear():
    isLeap = '윤년아님!'

    cond1 = (year % 4 == 0 and year % 100 != 0)
    cond2 = (year % 400 == 0)
    if cond1 or cond2: isLeap = '윤년 맞음!@@'

    print(f'{year} 년은 {isLeap} ')

# 데이터 입력 및 함수 호출
year = int(input('년도는? '))
isLeapYear(year)