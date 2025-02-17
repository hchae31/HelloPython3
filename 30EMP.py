# 성적 처리 프로그램 v7
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# CRUD 기능을 지원하는 성적처리 프로그램으로 재작성
# 즉, 성적 입력, 조회, 상세조회, 수정, 삭제 기능을 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 해당 명령 수행
# 학생 성적 데이터는 sungjuk 테이블에 저장

# 사원 데이터 기반 CRUD 기능이 제공되는 프로그램
# 사원  - empid,fname,lname,email,phone,hdate,jobid,sal,comm,mgrid,deptid
#
# 조회 - 사원번호,이름,이메일,부서번호,직책
# 상세조회 - 특정 사원번호 대상 모든 컬럼 출력

import sqlite3

# 데이터베이스 연결
# 사원등록프로그램

# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# CRUD 기능을 지원하는 성적처리 프로그램으로 재작성하기 위해
# 즉, 성적 입력, 상세조회, 수정, 삭제 기능을 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 해당 명령 수행
# 학생 성적 데이터는 sungjuk 테이블에 저장
# 3 layer architecture 방식으로 재작성
# 3layer =  presentation + business + database access
# SungJukV7b (P) - db/sungJukV7b (S) - db/sungjukv7bDAO (D)

import sys
import hchae31.emp as sjv7



# 메뉴 출력 및 메뉴별 처리
while True:
    # 메뉴 입력받음
    menu = emp.displayMenu()
    # 선택한 메뉴에 따라 해당 기능 수행
    if menu == '1':
        print('사원 데이터')
        e = emp.readEmp()
        emp.addEmp()
    elif menu == '2':
        print('사원데이터 조회')
        emp.showEmp()
    elif menu == '3':
        print('사원데이터 상세조회')
        pass
    elif menu == '4':
        print('사원 데이터 수정')
        pass
    elif menu == '5':
        print('사원 데이터 삭제')
        emp.removeEmp()
    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)
    else:
        print('메뉴를 잘못 선택하셨습니다!!')


# import sys
# import zzyzzy.sungjukv7 as sjv7
#
#
# # 메뉴 출력 및 메뉴별 처리
# while True:
#     # 메뉴 입력받음
#     menu = sjv7.displayMenu()
#
#     # 선택한 메뉴에 따라 해당 기능 수행
#     if menu == '1':
#         print('성적 데이터 추가')
#         sj = sjv7.readSungJuk()
#         sjv7.addSungJuk(sj)
#
#     elif menu == '2':
#         print('성적 데이터 조회')
#         sjv7.showSungJuk()
#
#     elif menu == '3':
#         print('성적 데이터 상세조회')
#         sjv7.showOneSungJuk()
#
#     elif menu == '4':
#         print('성적 데이터 수정')
#         pass
#     elif menu == '5':
#         print('성적 데이터 삭제')
#         pass
#     elif menu == '0':
#         print('프로그램 종료')
#         sys.exit(0)
#     else:
#         print('메뉴를 잘못 선택하셨습니다!!')
