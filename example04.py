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
    if cardno == 356317: result = 'JCB카드 NH농협카드'
    elif cardno == 356901: result = 'JCB카드 신한카드'
    elif cardno == 356912: result = '비자카드 신한카드'
elif cardno[:1] == '4':                       #cardno이 4로 시작하면?
    if cardno == 404825: result = '비자카드 KB국민카드'
    elif cardno == 438676: result = '마스터카드 신한카드'
elif cardno[:1] == '5':                       #cardno이 5로 시작하면?
    if cardno == 524353: result = '마스터카드 외환카드'
    elif cardno == 540926: result = '마스터카드 KB국민카드'

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
