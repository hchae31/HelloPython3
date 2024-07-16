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

