# 실전예제 1
email = 'gildong@abc123.co.kr'
name = '홍길동'
userid = 'gildong'
passwd = '1234'

# print(f'To. {email}')
# print(f'‣ 아이디 및 비밀번호 확인')
# print(f'‣ {name} 고객님 안녕하세요')
# print(f'‣ {name} 고객님 아이디와 비밀번호는 아래와 같습니다')
# print(f'‣ 아이디 : {userid}')
# print(f'‣ 비밀번호 : {passwd}')

print(f'''To. {email}
‣ 아이디 및 비밀번호 확인
{name} 고객님 안녕하세요
{name} 고객님 아이디와 비밀번호는 아래와 같습니다
아이디 : {userid}
비밀번호 : {passwd}''')

# 실전예제 2
day = input('요일은? ')
date = input('날짜(월일)는? ')
minTemp = input('최저 기온은? ')
maxTemp = input('최고 기온은? ')
rain = input('비올확률은?')
dusty = input('미세먼지는?')
riseSun = input('일출시간은?')
downSun = input('일몰시간은?')
southWave = input('남해 물결높이?')
southWave = input('동해 물결높이는?')
westWave = input('서해 물결높이는?')

print(f'''내일 날씨 예보입니다.
{day}요일인 {date}의 아침 최저 기온은 {minTemp}도, 낮 최고 기온은 {maxTemp}도로 예보 비올 확률은 {rain}%이고, 미세먼지는
{dusty} 수준일 것으로 예상됩니다. 일출 시간은 {riseSun}이고, 일몰 시간은 {downSun}입니다. 바다의 물결은 남해 앞바다 {southWave}m,
동해 앞바다 {southWave}m, 서해 앞바다 {westWave} 지금까지 {date} {day}요일 날씨 예보였습니다.''')

# 영수증 예제

# 3
rate1 = 123
# 1stPlayer = 456
# myprogram.java = 789
long = 987
# except = 654
TimeLimit = 321
numberOfWindows = 1000


# 4
# 예시로 5를 할당합니다. 다른 값을 할당할 수 있습니다.


# 12 - 생년월일 계산
# 연나이 계산 : 현재년도 - 태어난년도 (병역법,교육법,민방위)
# 만나이 : 현재년도 - 태어난년도, 생일안지남 (-1) (민법상, 2023-06부터)
# 한국식 나이 : 현재년도 - 태어난년도 + 1
currentYear = int(input('현재년도는? '))
birthyear = int(input('생일의 년도는? '))
myage = currentYear - birthyear

print(f'''현재년도는 {currentYear}이고, 생일의 년도가 {birthyear}일때, 나이는{myage} 입니다.''')

# 13 - 구구단7단 출력

# print('7 x 1 = 7')
# print('7 x 2 = 14')
# print('7 x 3 = 21')
# print('7 x 4 = 28')
# print('7 x 5 = 35')
# print('7 x 6 = 42')
# print('7 x 7 = 49')
# print('7 x 8 = 56')
# print('7 x 9 = 63')

dan = 7
print(f'{dan} x 1 = {dan*1}')
print(f'{dan} x 2 = {dan*2}')
print(f'{dan} x 3 = {dan*3}')
print(f'{dan} x 4 = {dan*4}')
print(f'{dan} x 5 = {dan*5}')
print(f'{dan} x 6 = {dan*6}')
print(f'{dan} x 7 = {dan*7}')
print(f'{dan} x 8 = {dan*8}')
print(f'{dan} x 9 = {dan*9}')

dan = 7
print(f'''
{dan} x 1 = {dan*1}
{dan} x 2 = {dan*2}
{dan} x 3 = {dan*3}
{dan} x 4 = {dan*4}
{dan} x 5 = {dan*5}
{dan} x 6 = {dan*6}
{dan} x 7 = {dan*7}
{dan} x 8 = {dan*8}
{dan} x 9 = {dan*9}''')