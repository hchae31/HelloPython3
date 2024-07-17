# 함수
# 특정 기능을 수행하는 코드블록(모음)에 이름을 부여한 것
# 즉, 여러 곳에 반복적으로 사용할 가치가 있는 코드들을
# 한 뭉치로 묶고 (어떤 값을 입력하면) 결과가 반환되도록
# 작성한 것 - 재사용이 주 목적
# 이처럼 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악가능
# 다른 사람과의 협업시 코드가 섞이지 않게 하기 위한
# 목적도 있음 - 모듈

print('오늘 날씨는 비옴!') # 단순 출력

print('오늘 날씨는 비옴!') # 반복 출력
print('오늘 날씨는 비옴!') # 단순 출력
print('오늘 날씨는 비옴!') # 단순 출력

for _ in range(3):      # 개선된 반복
    print('오늘 날씨는 비옴!')

# 만약, 이러한 반복문을 여러번 반복해야 한다면?
# 또, '비옴' 대신 '맑음' 이나 '흐림'으로 바꾸고 싶다면?
# => 함수를 이용!
# 함수 정의
# def 함수명(매개변수):
#       함수몸체

def say_weather():
    for _ in range(3):      # 개선된 반복
        print('오늘 날씨는 비옴!')

# 함수호출 1
# 함수명()

say_weather()

# 함수 정의 - 매개변수 선언
def say_weather(info):  # def : definition
    for _ in range(3):
        print(f'오늘 날씨는 {info}!')

# 함수 호출 2 - 함수명(인자)
say_weather('비옴')
say_weather('맑음')
say_weather('흐림')

# 단위 변환 : 인치 -> 센티미터
def convert_inch(inch):
    cm = inch * 2.54
    print(f'{inch} -> {cm}')




# def convert_centimeter(inch):
#     centi = inch * 2.54
#     print(f' {centi} cm')
#     return centi



