# while 문
# 조건을 만족할 때까지 반복 수행 - 반복횟수는 모름

# 변수 = 초기값
# while 조건식:
#    반복할문장
#    변수증가/감소

# 1 ~ 10 까지 정수 출력
# for i in range(1, 10+1):
#     print(i, end=' ')
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1

# 1 ~ 50 사이 정수 중 홀수만 출력
i = 1
while 1 <= 50:
    if i % 2 != 0:
        print(i, end=' ')
    i += 1

i = 1
while 1 <= 50:
    print(i, end=' ')
    i += 2
# for i in range(1,50+1,2):
#     print(i, end=' ')

# 1 ~ 50 사이 정수 중 9의 배수만 출력
i = 1
while i <= 50:
    if i % 9 == 0:
        print(i, end=' ')
    i += 1

# 반복문 내 실행 중지 : break
# for, while 문 내에서 반복흐름을 벗어나기 위해 사용



# 1 ~ 10000 사이 정수의 합을 출력
# 단, 정수의 합이 12345678보다 작으면 계산을 중지

sum = 0

for i in range(1, 10000+1):
    if sum > 12345678: break
    sum += i

print(sum, i)

# 1 ~ 10000 사이 정수의 합을 출력
# 단, 정수의 합이 12345678보다 작으면 계산을 중지 (while문으로)
i = 1
sum = 0
while i < 10000+1:
    if sum > 12345678: break
    sum += i
    i += 1

print(sum, i)

# 1 ~ 100사이 정수 중
# 3과 8의 공배수와 최소공배수 구하기
result = ''
for i in range(1, 100+1):
    if i % 3 == 0 and i % 8 == 0:
        result += f'{i} '

print(result, f'[{3 * 8}]')

# 삼각형 너비 계산하기
limitArea = 150  # 반복 중단 삼각형 너비
width = 2
height = 3
i = 1

while True:
    area = ((width * i) * (height * i)) / 2
    if area > limitArea : break
    print(f'삼각형 너비: {width * i} / {height * i}: {area}')
    i += 1


# i = 1
# width = 2*i
# height = 3*i
# while i < 20:
#     triangleArea = 0.5 * width * height
#     print(f'가로: {width}, 세로: {height}, 넓이 : {triangleArea}')
#     if triangleArea > 150:
#         print(f'삼각형의 넓이가 150보다 큽니다. 프로그램을 종료합니다.')
#         break
#     width += 2*i
#     height += 3*i
# print(width, height, triangleArea)


# 369 게임(while로 작성)
# 값 in str(문자열)
# '3' in str(36)
# '6' in str(36)
# '9' in str(12)

i = 1
while i < 100:
    jjak = ''
    if '3' in str(i): jjak += ' 짝!'
    if '6' in str(i): jjak += ' 짝!'
    if '9' in str(i): jjak += ' 짝!'
    if i == 33 or i == 66 or i == 99: jjak += ' 짝!'
    print(i, jjak)
    i += 1
# 열차 교차시간 만들기
trainA = 10
trainB = 25
trainC = 30
min = 1

while min < 541:
    for min in range(1, 540+1):
        if min % trainA == 0 and min % trainB == 0: # 50분간격
            hour = 9 + min // 60
            min = min % 60
            print(f'{hour}시 {min}분 : A - B 교차!')

        elif min % trainB == 0 and min % trainC == 0:
            hour = 9 + min // 60
            min = min % 60
            print(f'{hour}시 {min}분 : B - C 교차!')

        elif min % trainC == 0 and min % trainA == 0: # 30분간격
            hour = 9 + min // 60
            min = min % 60
            print(f'{hour}시 {min}분 : C - A 교차!')
    min += 1


# 로그인 기능 만들기
cntLogin = 1

while True:
    passwd = input('관리자 암호를 입력하세요. ')

    if passwd == 'hanbitac':
        isLogin = True
        print('로그인 되었습니다! ')
        break
    else:
        print('암호를 다시 입력하세요!')
    if cntLogin < 5: cntLogin += 1
    else:
        print('로그인 실패! 횟수 초과!')
        break
    cntLogin += 1
#