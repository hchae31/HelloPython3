
def displayMenu():
    main_menu = '''
    ==============================================
                성적 프로그램 v6
    ==============================================
        1. 성적 데이터 추가
        2. 성적 데이터 조회
        3. 성적 데이터 상세조회
        4. 성적 데이터 수정
        5. 성적 데이터 삭제
        0. 성적 데이터 종료
    ==============================================
     작업을 선택하세요 : 
    '''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu

# 성적 데이터 관련 변수 선언
sjs = []
# sjs = [ ['일지매',99,87,65,251,83.7,'우'] ]

# 성적 데이터를 입력 받는 함수

def readSungJuk():
    sj = []
    cnt = len(sjs)
    sj.append(input(f'{cnt}번학생 이름은 '))
    sj.append(int(input(f'{cnt+1}번학생 국어는? ')))
    sj.append(int(input(f'{cnt+1}번학생 영어는? ')))
    sj.append(int(input(f'{cnt+1}번학생 수학은? ')))
    return sj


# 입력받은 성적 데이터를 처리하고 리스트에 저장
def addSungJuk(sj):
    # sj = ['윤지', 99, 98, 99]
    sj.append(sj[1] + sj[2] + sj[3])
    # sj = ['윤지', 99ㅣ 98, 99, 297, 98.9, '수']
    sj.append(sj[4] / 3)
    # sj = ['윤지', 99ㅣ 98, 99, 297, 98.9, '수']
    grd = '수' if (sj[5] >= 90) else \
        '우' if (sj[5] >= 80) else \
        '미' if (sj[5] >= 70) else \
        '양' if (sj[5] >= 60) else '가'
    sj.append(grd)
    sjs.append(sj)
    saveSungJuk()


# 리스트에 저장된 성적 데이터를 중 기본 데이터만 모아서 출력
def showSungJuk():
    result = ''
    for sj in sjs:
        result += f'이름 : {sj[0]}, 국어: {sj[1]}, 영어: {sj[2]}, 수학: {sj[3]}, 총점: {sj[4]}, 평균: {sj[5]:2f}, 등급: {sj[6]}\n'
    print(result)

# sungjuk.dat에 저장된 성적데이터를 읽어서
# sjs 변수에 초기화
def loadSungJuk():
    with open('./hchae31/sungjuk.dat','w', encoding='UTF-8') as f:
        rows = f.readlines()

    for row in rows:
        data = row.split(',')
        sj = [d for d in data]
        sjs.append(sj)


# 메모리에 생성된 sjs변수의 모든 성적데이터를
# sungjuk.dat에 저장
def saveSungJuk():
    data = ''
    for sj in sjs:
        data += f'{sj[0]},{sj[1]},{sj[2]},{sj[3]},{sj[4]},{sj[5]},{sj[6]}\n'
    with open('./hchae31/sungjuk.dat', 'w', encoding='UTF-8') as f:
        f.write(data)

# 데이터 초기화 함수 호출
# loadSungJuk()
