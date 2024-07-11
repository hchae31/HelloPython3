# 성적 데이터 입력
name = input("이름을 입력하세요: ")
korean = int(input("국어 점수를 입력하세요: "))
english = int(input("영어 점수를 입력하세요: "))
math = int(input("수학 점수를 입력하세요"))

# 2. 성적처리
total = korean +  english + math
average = total / 3

# 학점 계산
if average >= 90:
    grade = "수"
elif average >= 80:
    grade = "우"
elif average >= 70:
    grade = "미"
elif average >= 60:
    grade = "양"
else:
    grade = "가"

# 3. 결과 출력
print(f"이름 : {name}")
print(f"국어 : {korean}, 영어: {english}, 수학: {math}")
print(f"총점 : {total}, 평균: {average:.If}, 학점: {grade}")