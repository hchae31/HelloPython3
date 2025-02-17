# 성적처리프로그램 v5
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# CRUD 기능을 지원하는 성적처리 프로그램으로 재작성하기 위해
# 즉, 성적 입력, 상세조회, 수정, 삭제 기능을 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 해당 명령 수행
# 학생 성적 데이터는 개별 변수가 아닌 리스트 안에 리스트 형태로 저장
# 리스트 형태로 저장된 성적데이터는 csv형식으로 변환해서 sungjuk.dat에 저장해 둠

import sys
import hchae31.sungJukv6 as sjv6


# # 프로그램 메뉴 정의
# main_menu = '''
# ==============================================
#             성적 프로그램 v3b
# ==============================================
#     1. 성적 데이터 추가
#     2. 성적 데이터 조회
#     3. 성적 데이터 상세조회
#     4. 성적 데이터 수정
#     5. 성적 데이터 삭제
#     0. 성적 데이터 종료
# ==============================================
#  작업을 선택하세요 :
# '''

# 성적 데이터 관련 변수 선언
sjs = [ ['일지매',99,87,65,251,83.7,'우'] ]

# 메뉴 출력 및 메뉴별 처리
while True:
    # 메뉴 입력받음
    menu = sjv6.displayMenu()

    # 선택한 메뉴에 따라 해당 기능 수행
    if menu == '1':
        print('성적 데이터 추가')
        sj = sjv6.readSungJuk()
        sjv6.addSungJuk(sj)

    elif menu == '2':
        print('성적 데이터 조회')
        sjv6.showSungJuk()

    elif menu == '3':
        print('성적 데이터 상세조회')
        pass
    elif menu == '4':
        print('성적 데이터 수정')
        pass
    elif menu == '5':
        print('성적 데이터 삭제')
        pass
    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)
    else:
        print('메뉴를 잘못 선택하셨습니다!!')


